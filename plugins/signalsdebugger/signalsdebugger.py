# -*- coding: utf-8 -*-
from pelican import signals

def pelican_initialized(*args, **kwargs):
    print args, kwargs

def get_generators(*args, **kwargs):
    print args, kwargs

def all_generators_finalized(*args, **kwargs):
    print args, kwargs

def get_writer(*args, **kwargs):
    print args, kwargs

def pelican_finalized(*args, **kwargs):
    print args, kwargs

def readers_init(*args, **kwargs):
    print args, kwargs

def generator_init(*args, **kwargs):
    print args, kwargs

def article_generator_init(*args, **kwargs):
    print args, kwargs

def article_generator_pretaxonomy(*args, **kwargs):
    print args, kwargs

def article_generator_finalized(*args, **kwargs):
    print args, kwargs

def article_generator_write_article(*args, **kwargs):
    print args, kwargs

def article_writer_finalized(*args, **kwargs):
    print args, kwargs

def page_generator_init(*args, **kwargs):
    print args, kwargs

def page_generator_finalized(*args, **kwargs):
    print args, kwargs

def page_writer_finalized(*args, **kwargs):
    print args, kwargs

def static_generator_init(*args, **kwargs):
    print args, kwargs

def static_generator_finalized(*args, **kwargs):
    print args, kwargs

def article_generator_preread(*args, **kwargs):
    print args, kwargs

def article_generator_context(*args, **kwargs):
    print args, kwargs

def page_generator_preread(*args, **kwargs):
    print args, kwargs

def page_generator_context(*args, **kwargs):
    print args, kwargs

def static_generator_preread(*args, **kwargs):
    print args, kwargs

def static_generator_context(*args, **kwargs):
    print args, kwargs

def content_object_init(*args, **kwargs):
    print args, kwargs

def content_written(*args, **kwargs):
    print args, kwargs

def feed_written(*args, **kwargs):
    print args, kwargs

def register():

    # Run-level signals:
    signals.initialized.connect(pelican_initialized)
    signals.get_generators.connect(get_generators)
    signals.all_generators_finalized.connect(all_generators_finalized)
    signals.get_writer.connect(get_writer)
    signals.finalized.connect(pelican_finalized)

    # Reader-level signals

    signals.readers_init.connect(readers_init)

    # Generator-level signals

    signals.generator_init.connect(generator_init)

    signals.article_generator_init.connect(article_generator_init)
    signals.article_generator_pretaxonomy.connect(article_generator_pretaxonomy)
    signals.article_generator_finalized.connect(article_generator_finalized)
    signals.article_generator_write_article.connect(article_generator_write_article)
    signals.article_writer_finalized.connect(article_writer_finalized)

    signals.page_generator_init.connect(page_generator_init)
    signals.page_generator_finalized.connect(page_generator_finalized)
    signals.page_writer_finalized.connect(page_writer_finalized)

    signals.static_generator_init.connect(static_generator_init)
    signals.static_generator_finalized.connect(static_generator_finalized)

    # Page-level signals

    signals.article_generator_preread.connect(article_generator_preread)
    signals.article_generator_context.connect(article_generator_context)

    signals.page_generator_preread.connect(page_generator_preread)
    signals.page_generator_context.connect(page_generator_context)

    signals.static_generator_preread.connect(static_generator_preread)
    signals.static_generator_context.connect(static_generator_context)

    signals.content_object_init.connect(content_object_init)

    # Writers signals
    signals.content_written.connect(content_written)
    signals.feed_written.connect(feed_written)
