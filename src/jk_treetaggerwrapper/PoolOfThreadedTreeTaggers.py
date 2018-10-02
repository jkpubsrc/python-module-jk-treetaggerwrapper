#!/usr/bin/python3


import time
import threading
import contextlib

import jk_utils

import treetaggerwrapper as ttpw



#
# This class wraps around tree taggers. It is best suitable for use in concurrent, multithreaded environments.
#
class PoolOfThreadedTreeTaggers(object):

	class _LangSpecificCache(object):

		def __init__(self, langID:str):
			self.langID = langID
			self.idleInstances = []
			self.lastAccess = time.time()
			self.countUsedInstances = 0
			self.langLock = threading.Lock()
		#

		def touch(self):
			self.lastAccess = time.time()
		#
	#

	################################################################
	#### Constructors / Destructors
	################################################################

	def __init__(self, treeTaggerInstallationPath:str):
		self.__treeTaggerInstallationPath = treeTaggerInstallationPath
		self.__unused = {}
		self.__onTaggerCreated = jk_utils.ObservableEvent("onTaggerCreated")

		self.__mainLock = threading.Lock()
	#

	################################################################
	#### Events
	################################################################

	#
	# This property returns an event object. Whenever a new TreeTagger process is created, this event is fired.
	#
	@property
	def onTaggerCreated(self):
		return self.__onTaggerCreated
	#

	################################################################
	#### Methods
	################################################################

	#
	# This method must be used together with the "with" statement to retrieve and use a <c>treetaggerwrapper</c> object.
	#
	# Have a look at <c>tagText()</c>: That method might be exactly what you are looking for as <c>tagText()</c> is implemented as this:
	#
	# <code>
	#	def tagText(self, langID:str, text:str) -> str:
	#		with self._useTagger(langID) as tagger:
	#			return tagger.tag_text(text)
	# </code>
	#
	@contextlib.contextmanager
	def _useTagger(self, langID:str):
		assert isinstance(langID, str)

		with self.__mainLock:
			langIDCache = self.__unused.get(langID, None)
			if langIDCache is None:
				langIDCache = PoolOfThreadedTreeTaggers._LangSpecificCache(langID)
				self.__unused[langID] = langIDCache

		langIDCache.touch()

		if langIDCache.idleInstances:
			with langIDCache.langLock:
				tagger = langIDCache.idleInstances[-1]
				del langIDCache.idleInstances[-1]
				langIDCache.countUsedInstances += 1
		else:
			tagger = ttpw.TreeTagger(
				TAGLANG=langID,
				TAGOPT="-prob -threshold 0.7 -token -lemma -sgml -quiet",
				TAGDIR=self.__treeTaggerInstallationPath)
			self.__onTaggerCreated.fire(self, langID)
			with langIDCache.langLock:
				langIDCache.countUsedInstances += 1

		try:
			yield tagger
		finally:
			with langIDCache.langLock:
				langIDCache.countUsedInstances -= 1
				langIDCache.idleInstances.append(tagger)
	#

	#
	# Convenience method that grabs a free instance of a suitable <c>TreeTagger</c>, tags the data, returns the tree tagger instance used
	# and then returns the tagging result to the caller.
	#
	def tagText(self, langID:str, text:str) -> str:
		assert isinstance(text, str)

		with self._useTagger(langID) as tagger:
			return tagger.tag_text(text)
	#

	#
	# Retrieve statistical information about the tagging instances maintained in the background.
	#
	def getStats(self):
		with self.__mainLock:
			allTuples = list(self.__unused.items())

		ret = {}
		for langID, langIDCache in allTuples:
			ret[langID] = {
				"idle": len(langIDCache.idleInstances),
				"inUse": langIDCache.countUsedInstances
			}
		return ret
	#

#








