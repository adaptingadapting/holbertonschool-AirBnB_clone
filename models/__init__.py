#!/usr/bin/python3
""" init module, modified """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
