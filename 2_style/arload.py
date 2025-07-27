import os
import re
import sys
import shutil
import getpass
import datetime
import subprocess

import libLog
import libData
import libFunc
import arNotice
import arSaveAs

from arUtil import ArUtil
from tank import Tank
from Qt import QtWidgets, QtGui, QtCore, QtCompat

TITLE = "load"
LOG = libLog.init(script=TITLE)

global main_widget

class ArLoad(ArUtil):
    def __init__(self):
        super().__init__()
        path_ui = os.path.join(os.path.dirname(__file__), "ui", TITLE + ".ui")
        self.wgLoad = QtCompat.loadUi(path_ui)
        self.load_dir = ''
        self.load_file = ''
        self.software_format = {y:x.upper() for x,y in self.data['software']['EXTENSION'].items()}
        self.software_keys = list(self.software_format.keys())
    
    def setup(self):
        #start commands
        self.wgLoad.lstScene.clear()
        self.wgLoad.lstStatus.clear()
        self.wgLoad.lstSet.clear()
        self.clear_meta()
        self.resize_widget(self.wgLoad)
        self.wgLoad.show()
        LOG.info('START : ArLoad')


    def press_btnAccept(self):
        if not os.path.exists(self.load_file):
            self.set_status(
                'FAILED LOADING : Path doesn\'t exists: {}'.format(self.load_file),
                  msg_type=3)
            return False
    
    def press_menuItemAddFolder(self):
        self.save_as = arSaveAs.start(new_file=False)
    
    def press_menuSort(self, list_widget, reverse=False):
        file_list = []
       
        for index in range(list_widget.count()):
             file_list.append(list_widget.item(index).text())
        
        list_widget.clear()
        list_widget.addItems(sorted(file_list, reverse=reverse))
   
    def change_lstScene(self):
        currentScene = self.wgLoad.lstScene.currentItem().text()
        self.load_dir = self.data['project']['PATH'][currentScene]
        tmp_content = libFunc.get_file_list(self.load_dir)
        self.scene_steps = len(
            self.data['rules']['SCENES'][currentScene].split('/'))
        
        if self.scene_steps < 5:
            self.wgLoad.lstAsset.hide()
        else:
            self.wgLoad.lstAsset.itemSelectionChanged.connect(self.change_lstAsset)
            self.wgLoad.lstAsset.show()
       
        self.wgLoad.lstSet.clear()
        if tmp_content:
            self.wgLoad.lstSet.addItems(sorted(tmp_content))
            self.wgLoad.lstSet.setCurrentRow(0)
    
    def change_lstSet(self):
        new_path = os.path.join(
            self.load_dir, self.wgLoad.lstSet.currentItem().text()
        )
        tmp_content = libFunc.get_file_list(new_path)
       
        if self.scene_steps < 5:
            self.wgLoad.lstTask.clear()
            if tmp_content:
                self.wgLoad.lstTask.addItems(sorted(tmp_content))
                self.wgLoad.lstTask.setCurrentRow(0)
        else:
            self.wgLoad.lstAsset.clear()
            if tmp_content:
                self.wgLoad.lstAsset.addItems(sorted(tmp_content))
                self.wgLoad.lstAsset.setCurrentRow(0)
    
    def change_lstAsset(self):
        new_path = os.path.join(
            self.load_dir,
            self.wgLoad.lstSet.currentItem().text(),
            self.wgLoad.lstAsset.currentItem().text()
        )
        tmp_content = libFunc.get_file_list(new_path)
        self.wgLoad.lstTask.clear()
       
        if tmp_content:
            self.wgLoad.lstTask.addItems(sorted(tmp_content))
            self.wgLoad.lstTask.setCurrentRow(0)
    
    def fill_meta(self):
        self.wgPreview.lblTitle.setText(self.file_name)
        self.wgPreview.lblDate.setText(
            str(datetime.datetime.fromtimestamp(os.path.getmtime(self.load_file)))
            .split(".")[0]
        )
        size_mb = os.path.getsize(self.load_file) / (1024 * 1024.0)
        self.wgPreview.lblSize.setText(str("{0:.2f}".format(size_mb) + " MB"))
    
    def clear_meta(self):
        self.wgPreview.lblUser.setText('')
        self.wgPreview.lblTitle.setText('')
        self.wgPreview.lblDate.setText('')

    
def start():
    main_widget = ArLoad()
    main_widget.setup()
