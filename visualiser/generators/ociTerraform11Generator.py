# Copyright (c) 2013, 2014-2019 Oracle and/or its affiliates. All rights reserved.


"""Provide Module Description
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
__author__ = ["Andrew Hopkinson (Oracle Cloud Solutions A-Team)"]
__copyright__ = "Copyright (c) 2013, 2014-2019  Oracle and/or its affiliates. All rights reserved."
__version__ = "1.0.0.0"
__date__ = "@BUILDDATE@"
__status__ = "@RELEASE@"
__module__ = "ociTerraform11Generator"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


import datetime
import getopt
import jinja2
import json
import locale
import logging
import operator
import os
import requests
import sys

from generators.ociGenerator import OCIGenerator

from common.ociCommon import readJsonFile
from common.ociCommon import readYamlFile
from common.ociCommon import writeTerraformFile
from common.ociLogging import getLogger

# Configure logging
logger = getLogger()

class OCITerraform11Generator(OCIGenerator):
    DIRECTORY_SUFFIX = 'terraform11'
    MAIN_FILE_NAME = 'main.tf'
    VARIABLES_FILE_NAME = 'variables.tf'
    TERRAFORM_FILE_NAME = 'terraform.tfvars'
    OUTPUTS_FILE_NAME = 'output.tf'
    JINJA2_VARIABLE_FORMAT = '${{var.{0:s}}}'

    def __init__(self, template_root, output_root, visualiser_json):
        template_dir = os.path.join(template_root, self.DIRECTORY_SUFFIX)
        output_dir = os.path.join(output_root, self.DIRECTORY_SUFFIX)
        logger.info('OCITerraform11Generator : Template Directory {0!s:s}'.format(template_dir))
        logger.info('OCITerraform11Generator : Output Directory {0!s:s}'.format(output_dir))
        super(OCITerraform11Generator, self).__init__(template_dir, output_dir, visualiser_json)

    def writeFiles(self):
        main_rendered = self.getRenderedMain()
        # Write Main tf processing file
        writeTerraformFile(os.path.join(self.output_dir, self.MAIN_FILE_NAME), main_rendered)
        # Write Variable files
        variable_definitions = []
        variable_values = []
        for key, value in self.getVariables().items():
            variable_values.append('{0!s:s} = "{1}"'.format(key, value))
            variable_definitions.append('variable "{0:s}" {{}}'.format(key))
            #variable_definitions.append('variable "{0:s}" {{\ndefault = "{1}"\n}}'.format(key, value))
        writeTerraformFile(os.path.join(self.output_dir, self.VARIABLES_FILE_NAME), variable_definitions)
        writeTerraformFile(os.path.join(self.output_dir, self.TERRAFORM_FILE_NAME), variable_values)

        return

    def formatJinja2Variable(self, variable_name):
        return '${{var.{0:s}}}'.format(variable_name)

    def formatJinja2IdReference(self, resource_name):
        return '${{local.{0:s}_id}}'.format(resource_name)

    def formatJinja2DhcpReference(self, resource_name):
        return '${{local.{0:s}_dhcp_options_id}}'.format(resource_name)


