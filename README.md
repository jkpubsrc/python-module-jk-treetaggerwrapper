jk_treetaggerwrapper
====================

Introduction
------------

This python module provides a wrapper around `treetaggerwrapper` which in turn is a Python based wrapper around the `TreeTagger` PoS-tagger.

This might sound a bit strange in the first place, but actually, there is a simple reason for that approach: The `treetaggerwrapper` is designed as a non-concurrent wrapper. In various application this is a limitation you might not be willing to take. This module wraps a management class around the `treetaggerwrapper` which will enable concurent and even multithreaded execution.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-treetaggerwrapper)
* [pypi.python.org](https://pypi.python.org/pypi/jk_treetaggerwrapper)

How to use this module
----------------------

Example:

```python
pool = PoolOfThreadedTreeTaggers("/path/to/treetagger")

result = pool.tagText("en", "The sun is shining and the children are smiling.")
```

In order to tag a text you first need to instantiate a pool of taggers. Then you can invoke `tagText()` in order to temporarily allocate an instance of `TreeTagger` in the background and perform the PoS tagging.

Concurrency
-----------

Please note that this library is based on `treetaggerwrapper` which follows a thread-based concurrency model. On tagging `treetaggerwrapper` instantiates a TreeTagger background process that is alive for the duration of the `treetaggerwrapper` object. This `treetaggerwrapper` object then communicates with this background process and uses threads for this purpose. Therefor the class `PoolOfThreadedTreeTaggers` provided by `jk_treetaggerwrapper` is bound to this limitation.

Further Information
-------------------

### TreeTagger

* http://cental.fltr.ucl.ac.be/team/~panchenko/def/treetagger/

### treetaggerwrapper

* https://pypi.org/project/treetaggerwrapper/
* https://subversion.renater.fr/ttpw/trunk/
* https://treetaggerwrapper.readthedocs.io/en/latest/

Contact Information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



