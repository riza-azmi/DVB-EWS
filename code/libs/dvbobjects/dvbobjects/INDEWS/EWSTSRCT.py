#! /usr/bin/env python

# This file is part of the dvbobjects library.
# 
# Copyright � 2004, Lorenzo Pallara
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import string
from dvbobjects.MPEG.Section import Section
from dvbobjects.utils import *



######################################################################
class ews_tsrct_section(Section):

    """
	expects the following variable
	
	    ews_tolal_map_item  	- 2 bytes
	    
	    each ection contains only max 10 codes    
    """


    table_id = 0x80
    section_max_size = 1024

    def pack_section_body(self):
    
        # pack program_loop_item
        pl_bytes = string.join(
            map(lambda x: x.pack(),
                self.ews_tsrct_loop),
            "")

        self.table_id_extension = 0x04
	self.private_indicator = 0

        fmt = "!HB%ds" % (len(pl_bytes))
        return pack(fmt,
    	    self.ews_total_map_item,
    	    len(self.ews_tsrct_loop),
            pl_bytes
            )
            

######################################################################
class ews_tsrct_code_item(DVBobject):
    """
	expects the following variable
	
	    ews_region_code	- 2 bytes
    """

    def pack(self):
    
        # pack program_loop_item
        fmt = "!H"
	return pack(fmt,
	    self.ews_region_code,
	)

            

######################################################################
class ews_tsrct_loop_item(DVBobject):

    """
	expects the following variable
	
	    ews_tsstream_id 		- 2 bytes
	    	    
	    ews_region_code_list	- 2 bytes each
	
    """


    def pack(self):

        pl_bytes = string.join(
            map(lambda x: x.pack(),
                self.ews_tsrct_code_loop),
            "")
    
        # pack program_loop_item
        fmt = "!HH%ds" % (len(pl_bytes)) 
	return pack(fmt,
	    self.ews_tsstream_id,
	    len(self.ews_tsrct_code_loop),
	    pl_bytes
	)




