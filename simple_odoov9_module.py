#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print "*****************************************************************"
print "*        Simple Odoo v9 module generator for foundation         *"
print "*        Kirirom Institute of Technology                        *"
print "*        Owner: Duk Panhavad                                    *"
print "*        Mail: dukpanhavad@kit.edu.kh                           *"
print "*****************************************************************"

# Config module information
input_name = raw_input("Enter module name: ")
author_name = raw_input("Enter author name: ")
company_name = raw_input("Enter the company you from: ")
website_name = raw_input("Enter the official website: ")
cate_name = raw_input("Enter the category name: ")
purpose_name = raw_input("What is the purpose of creating this module?\nAnswer:")
cant_campos = int(raw_input("Number of field: "))
print "\n******************* Field configuration ***********************\n"

# Folder creation
os.makedirs(input_name)
os.makedirs(input_name + "/views")
os.makedirs(input_name + "/models")

# File creation
# Create file __init__.py and configuration
m_file = open(input_name + '/__init__.py', 'w')
m_file.write('# -*- coding: utf-8 -*- \n')
m_file.write('import models \n')
m_file.close()

# Create file __openerp__.py and configuration
m_file = open(input_name + '/__openerp__.py', 'w')
m_file.write('# -*- coding: utf-8 -*-\n')
m_file.write('##############################################################################\n')
m_file.write('#\n')
m_file.write('#    This module copyright (C) 2017 Duk Panhavad\n')
m_file.write('#\n')
m_file.write('#    This program is free software: you can redistribute it and/or modify\n')
m_file.write('#    it under the terms of the GNU Affero General Public License as\n')
m_file.write('#    published by the Free Software Foundation, either version 3 of the\n')
m_file.write('#    License, or (at your option) any later version.\n')
m_file.write('#\n')
m_file.write('#    This program is distributed in the hope that it will be useful,\n')
m_file.write('#    but WITHOUT ANY WARRANTY; without even the implied warranty of\n')
m_file.write('#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n')
m_file.write('#    GNU Affero General Public License for more details.\n')
m_file.write('#\n')
m_file.write('#    You should have received a copy of the GNU Affero General Public License\n')
m_file.write('#    along with this program.  If not, see <http://www.gnu.org/licenses/>.\n')
m_file.write('#\n')
m_file.write('##############################################################################\n')
m_file.write('{\n')
m_file.write('    \'name\': \'' + input_name + ' \',\n')
m_file.write('    \'version\': \'9.0.0.1.0\',\n')
m_file.write('    \'author\': \'' + author_name + ' \',\n')
m_file.write('    \'from\': \'' + company_name + ' \',\n')
m_file.write('    \'website\': \'' + website_name + ' \',\n')
m_file.write('    \'license\': \'AGPL-3\',\n')
m_file.write('    \'category\': \'' + cate_name + ' \',\n')
m_file.write('    \'summary\': \'' + purpose_name + ' \',\n')
# m_file.write('    \'depends\': [\'account\',\'account_accountant\'],\n')
m_file.write('    \'description\': "Duk Panhavad owned tool generator""\n')
m_file.write('Module generator solution\n')
m_file.write('===================================================== \n')
m_file.write('Thank you for using this as part of your project\n')
m_file.write('""",\n')
m_file.write('    \'demo\': [],\n')
m_file.write('    \'test\': [],\n')
m_file.write('    \'data\': [\'views/' + input_name + '_view.xml\',],\n')
m_file.write('    \'installable\': True,\n')
m_file.write('    \'auto_install\': False,\n')
m_file.write('}\n')
m_file.close()

# Model creation
m_file = open(input_name + '/models/__init__.py', 'w')
m_file.write('# -*- coding: utf-8 -*- \n')
m_file.write('import ' + input_name + ' \n')
m_file.close()

# Model configuration
m_file = open(input_name + '/models/' + input_name + '.py', 'w')
m_file.write('# -*- coding: utf-8 -*- \n')
m_file.write('# Part of Odoo. See LICENSE m_file for full copyright and licensing details. \n')
m_file.write('from openerp import api, fields, models \n')
m_file.write('from datetime import datetime \n')
m_file.write('\n')
m_file.write('class ' + input_name + '(models.Model): \n')
m_file.write('    _name = \'dp.' + input_name + '\' \n')
arrangement = []
for num in range(1, cant_campos + 1):
    field_name = raw_input("Field name:")
    print "Char,Text,Boolean,Datetime,Integer"
    field_type = raw_input("Field type:")
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n\n"
    m_file.write('    ' + field_name + ' = fields.' + field_type + '(string=\'' + field_name + '\', required=True) \n')
    m_file.write(' \n')
    arrangement.append(field_name)
m_file.close()

# Create file _views.xml
m_file = open(input_name + '/views/' + input_name + '_view.xml', 'w')
m_file.write('<?xml version="1.0" encoding="UTF-8"?> \n')
m_file.write('<openerp> \n')
m_file.write('<!-- Comment on view --> \n')
m_file.write('     <record id="view_dp_' + input_name + '_form" model="ir.ui.view"> \n')
m_file.write('        <field name="name">dp.' + input_name + '.form</field> \n')
m_file.write('        <field name="model">dp.' + input_name + '</field> \n')
m_file.write('        <field name="arch" type="xml"> \n')
m_file.write('            <form string="List of ' + input_name.capitalize() + '"> \n')
m_file.write('                <group> \n')
for field_name in arrangement:
    m_file.write('                    <field name="' + field_name + '"/> \n')
m_file.write('                </group> \n')
m_file.write('            </form> \n')
m_file.write('        </field> \n')
m_file.write('    </record> \n')

m_file.write('     <record id="view_dp_' + input_name + '_tree" model="ir.ui.view"> \n')
m_file.write('        <field name="name">dp.' + input_name + '.tree</field> \n')
m_file.write('        <field name="model">dp.' + input_name + '</field> \n')
m_file.write('        <field name="arch" type="xml"> \n')
m_file.write('           <tree> \n')
for field_name in arrangement:
    m_file.write('                    <field name="' + field_name + '"/> \n')
m_file.write('           </tree> \n')
m_file.write('        </field> \n')
m_file.write('    </record> \n')

# Action configuration
m_file.write('    <record model="ir.actions.act_window" id="act_dp_' + input_name + '"> \n')
m_file.write('        <field name="name">' + input_name + '</field> \n')
m_file.write('        <field name="type">ir.actions.act_window</field> \n')
m_file.write('        <field name="res_model">dp.' + input_name + '</field> \n')
m_file.write('        <field name="view_type">form</field> \n')
m_file.write('        <field name="view_mode">tree,form</field> \n')
m_file.write('    </record> \n')

# Menu configuration
m_file.write('<!--  Menu declaration --> \n')
m_file.write('<menuitem id="dp_' + input_name + '_menu" name="' + input_name.capitalize() + '" sequence="10"/> \n')
m_file.write(
    '<menuitem id="submenu_dp_' + input_name + '_menu" name="' + input_name.capitalize() + '" sequence="10" parent="dp_' + input_name + '_menu"/> \n')
m_file.write(
    '<menuitem id="submenu_dp_' + input_name + '_action" name="' + input_name.capitalize() + '" sequence="10" parent="submenu_dp_' + input_name + '_menu" action="act_dp_' + input_name + '"/> \n')

m_file.write('</openerp> \n')
m_file.close()

print "Module successfully created as " + input_name
