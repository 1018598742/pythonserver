#!/usr/bin/env python3
# _*_ coding = utf-8 _*_
from www.orm import Model, StringField, IntegerField


class Runoob(Model):
    __table__ = 'runoob_tb1'
    runoob_id = IntegerField(primary_key=True)
    runoob_title = StringField(ddl='varchar(100)')
    runoob_author = StringField(ddl='varchar(40)')
    submission_date = StringField(ddl='varchar(20)')