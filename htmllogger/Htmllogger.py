import os, sys
from datetime import datetime
import time
import random
import inspect
import platform
import getpass
import socket
import inspect
from distutils.dir_util import copy_tree

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class HTMlLogger(metaclass=Singleton):

    f = open(os.getcwd() + "report.html", "a")
    filepath = ""
    parentid = ""
    rowid = ""
    childid = ""

    def __init__(self, reportpath):
        self.filepath = reportpath
        # for arg in args:
        #     if arg != "":
        #         self.filepath = arg
        #         break
        # if args.__len__()==0:
        #     self.filepath = str(os.path.dirname(os.path.abspath(__file__)))+"\..\.."
        if not(self.filepath.find("Reports")!=-1):
            if not os.path.exists(self.filepath + "/Reports"):
                os.mkdir(self.filepath + "/Reports")
            self.filepath = self.filepath + "/Reports"
        else:
            if not os.path.exists(self.filepath):
                os.mkdir(self.filepath)


        if not os.path.exists(self.filepath+"/css"):
            copy_tree(str(os.path.dirname(os.path.abspath(__file__)))+'/css',self.filepath+"/css")


        repfld = self.filepath
        print(repfld)
        self.filepath = self.filepath + "/report_" + str(time.strftime("%Y%m%d-%H%M%S")) + ".html"
        self.f = open(self.filepath, "w+")
        support_logger().create_support(repfld)
        print('i am htmllogger called')
        strStartFile = """<html>
        	<head>
        	    <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1">

        		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.1/jquery-ui.min.js"></script>
        		<script type="text/javascript" src="./css/jquery.tbltree.js"></script>
        		<link type="text/css" href="css/jquery.tbltree.css" rel="stylesheet">
        		<script type="text/javascript" src="./css/jquery.cookie.js"></script>
				<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

        		<script type="text/javascript">
        		  $(function() {
        			 // initialize with default options
        			$( "#table1" ).tbltree();
        		  });
				  google.charts.load("current", {packages:["corechart"]});
				  google.charts.setOnLoadCallback(drawChart);
				  function openTab(evt, cityName) {
					  var i, tabcontent, tablinks;
					  tabcontent = document.getElementsByClassName("maincontent");
					  for (i = 0; i < tabcontent.length; i++) {
						tabcontent[i].style.display = "none";
					  }
					  tablinks = document.getElementsByClassName("tablinks");
					  for (i = 0; i < tablinks.length; i++) {
						tablinks[i].className = tablinks[i].className.replace(" active", "");
					  }
					  document.getElementById(cityName).style.display = "";
					  evt.currentTarget.className += " active";
				}
				function load(){
				document.getElementById("defaultOpen").click();
				}
				function calcFail()
				{

					var elements = document.getElementsByClassName("fail");
					var names = '';
					for(var i=0; i<elements.length; i++) {
						names = elements[i].getAttribute('parentid');
						document.getElementById(names).innerHTML="<img src='css/images/fail_4.png'/>&nbsp FAIL";
						document.getElementById(names).setAttribute("class", "testFAIL"); 
					}

				}
				function drawChart() {
				    var pass  = document.getElementsByClassName("testPASS").length
					var fail  = document.getElementsByClassName("testFAIL").length
					//var norun = 1
					var data = google.visualization.arrayToDataTable([
					  ['Task', 'Hours per Day'],
					  ['PASS',     pass],
					  ['FAIL',      fail],
					//  ['No Run',   norun],

					]);

					var options = {

					  pieHole: 0.5,

					  colors: ['green', '#FF0000', '#3498db']
					};

					var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
					chart.draw(data, options);
				  }
        		</script>
        		<style>
					#sidebar {
						width: 15%;
						height: 100%;
						position: fixed;
						background:  #454545; /*#2f323a*/
						left: 0;
					}

					.nav-collapse.collapse {
						display: inline;
					}

					ul.sidebar-menu , ul.sidebar-menu li ul.sub{
						margin: -2px 0 0;
						padding: 0;
					}

					ul.sidebar-menu {
						margin-top: 75px;
					}

					#sidebar > ul > li > ul.sub {
						display: none;
					}

					#sidebar > ul > li.active > ul.sub, #sidebar > ul > li > ul.sub > li > a {
						display: block;
					}

					ul.sidebar-menu li ul.sub li{
						background: white;
						margin-bottom: 0;
						margin-left: 0;
						margin-right: 0;
					}

					ul.sidebar-menu li ul.sub li:last-child{
						border-radius: 0 0 4px 4px;
						-webkit-border-radius: 0 0 4px 4px;
					}

					ul.sidebar-menu li ul.sub li a {
						font-size: 12px;
						padding: 6px 0;
						line-height: 35px;
						height: 35px;
						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
						color: #fcfffa;
					}

					ul.sidebar-menu li ul.sub li a:hover {
						color: white;
						background: transparent;
					}

					ul.sidebar-menu li ul.sub li.active a {
						color: white;
						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
						display: block;
					}

					ul.sidebar-menu li{
						line-height: 20px !important;
						margin-bottom: 5px;
						margin-left:0px;
						margin-right:10px;
					}

					ul.sidebar-menu li.sub-menu{
						line-height: 15px;
					}

					ul.sidebar-menu li a span{
						display: inline-block;
						color: white;
					}

					ul.sidebar-menu li a{
						color: #fcfffa;
						text-decoration: none;
						display: block;
						padding: 15px 10px 15px 10px;
						font-size: 12px;
						font-color:white
						outline: none;
						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
					}

					ul.sidebar-menu li a.active, ul.sidebar-menu li a:hover, ul.sidebar-menu li a:focus {
						background: #999999;
						color: #fff;
						display: block;

						-webkit-transition: all 0.3s ease;
						-moz-transition: all 0.3s ease;
						-o-transition: all 0.3s ease;
						-ms-transition: all 0.3s ease;
						transition: all 0.3s ease;
					}


					ul.sidebar-menu li a i {
						font-size: 15px;
						padding-right: 6px;
					}

					ul.sidebar-menu li a:hover i, ul.sidebar-menu li a:focus i {
						color: #fff;
					}

					ul.sidebar-menu li a.active i {
						color: #fff;
					}

					 #rcorners2 {
                      border-radius: 25px;
                      border: 4px solid #22242a; /*  #73AD21*/
                      box-shadow: 5px
                      padding: 0px; 
                      width: 80%;  
                    }
                    #table1 {

                      box-shadow: 5px
                      padding: 0px; 
                      width:70%;
					  isplay: inline-block;

                    }
                     #fail{
					  align:center
					}
					.img-circle {

						border-radius: 50%;
							border-top-left-radius: 50%;
							border-top-right-radius: 50%;
							border-bottom-right-radius: 50%;
							border-bottom-left-radius: 50%;
					}

					.header{

						background: #454545;
						border-bottom: 1px solid #454545;
						height: 3%;
						position: fixed;
						left: 0;
						top: 0;
						right: 0;
						z-index: 1002;
					}
					.logo{
					   background: #4ECDC4;
					   size:12px;
					}
					.logo1{
					   background: White;
					   size:13px;
					}
					.container{
					  /* background: white;*/
					  background : #f1f1f1;
					}
					.maincontent{
					  display: inline-block;
					 margin-top: 1%;

					  /* padding-left: 1px;*/
					  padding-right: 15px;
					  padding-bottom: 15px;
					  padding-top: 0px;
					  width: 100%;
					}
					#detailedreport{
					  padding-left: 2px;

					}
                    #dashboard{
					  padding-top: 0px;
					}
                    .data{
					  width : 100px;
					}
                    #EnvDet{
					  width: 320px;
					  padding: 10px;
					  border: 5px solid gray;
					  margin: 0;
					}
					#ExeDet{
					  width: 320px;
					  padding-left: 10%;
					  border: 5px solid gray;
					  margin: 0;
					}
					#th{
					   font-size: 23px;
					}					
        		</style>
        	</head>

        <body onload="load();calcFail()" >

    <!-- **********************************************************************************************************************************************************
        TOP BAR CONTENT & NOTIFICATIONS
        *********************************************************************************************************************************************************** -->
    <!--header start-->
    <header class="header">
      <div class="sidebar-toggle-box">
        <div class="fa fa-bars tooltips" data-placement="right" data-original-title="Toggle Navigation"></div>
      </div>
      <!--logo start-->


    </header>
		  <div id="sidebar" class="nav-collapse ">
				<!-- sidebar menu start-->
				<ul class="sidebar-menu" id="nav-accordion">
				  <p class="centered" align="Center"><img src="css/images/logo.png" class="img-circle" width="80px"></p>
				  <p align="Center"><b><font size=6 color="White" >HTMLLogger</font></b></p>
				  <li class="mt">
					<a class="tablinks" onclick="openTab(event, 'dashboard')" id="defaultOpen">
					  <i class="fa fa-dashboard"></i>
					  <span >Dashboard</span>
					  </a>
				  </li>
				  <li class="sub-menu">
					<a onclick="openTab(event, 'detailedreport')" class="tablinks">
					  <i class="fa fa-desktop"></i>
					  <span>Detailed Report</span>
					  </a>
				  </li>
				  <li class="sub-menu">
					<a onclick="openTab(event, 'envdetails')" class="tablinks">
					  <i class="fa fa-cogs"></i>
					  <span>Environment Details</span>
					  </a>
				  </li>
				</ul>			
      </div>
       <div id="envdetails" class="maincontent" style="width: 900px; height: 500px; padding-left: 15%;" >
	      <p><h1  id = 'EnvDet'><b>Environment Details</b></h1></p>
		  <p><b> OS Name : </b>""" + platform.system() + """</p>
		  <p><b> OS Release : </b>""" + platform.release() + """</p>
		  <p><b> Machine Name :</b>""" + socket.gethostname() + """</p>
		  <p><b> User Name : </b>""" + getpass.getuser() + """ </p>
	  </div>
	  <div id="dashboard" class="maincontent" style="padding-left: 15%;">
	      <p><h1  id = 'EnvDet'><b>Summary</b></h1></p>
		  <div id="donutchart" style="width: 700px; height:500px;"></div>
	  </div>

      <div class="maincontent" id="detailedreport">

          <table id="table1" border=1 align=Center class="container">
          <tr>
          <th id='th'>Test Case Name</th><th id='th' >Status</th><th id='th'>Time </th>
  </tr>"""
        self.f.writelines(strStartFile)
        self.f.close()
        # print(inspect.stack()[1][0].f_code.co_name)

    def assert_testcase_log(self, log):

        self.f = open(self.filepath, "a")
        self.parentid = random.randrange(0, 6000, 1)
        tlog = """
              <tr row-id='""" + str(self.parentid) + """'>
                <td><b>""" + log + """</b></td><td class="testPASS" id = '""" + str(
            self.parentid) + """'><img src="css/images/pass_4.png"/>&nbsp PASS</td><td class="data">""" + str(
            time.strftime("%H:%M:%S")) + """</td>
              </tr>
            """
        self.f.writelines(tlog)
        self.f.close()
        # print(self.__doc__)

    def assert_step_log(self, log):
        self.f = open(self.filepath, "a")
        self.rowid = random.randrange(6000, 200000, 1)

        tlog = """
                      <tr row-id='""" + str(self.rowid) + """' parent-id='""" + str(self.parentid) + """'>
                        <td>""" + log + """</td><td class="data"><img src="css/images/pass_4.png"/>&nbsp PASS</td><td class="data">""" + str(
            time.strftime("%H:%M:%S")) + """</td>
                      </tr>
                    """
        self.f.writelines(tlog)
        self.f.close()

    def assert_step_fail_log(self, driver, log):
        self.f = open(self.filepath, "a")
        self.childid = random.randrange(20000, 60000, 1)
        img = self.filepath.split("/")[len(self.filepath.split("/")) - 1]
        snappath = self.filepath.replace(self.filepath.split("/")[len(self.filepath.split("/")) - 1],"")
        if not os.path.exists(snappath+"/FailureImages"):
            os.mkdir(snappath+"/FailureImages")
        snappath = snappath+"/FailureImages"

        img = img.replace("html", "png")
        #snappath = snappath.replace("LatestTree", "FailureImg")
        img = img.replace("report_", "snap_")
        strP = img #snappath.split("/")[len(snappath.split("/")) - 1]
        # snappath.replace("LatestTree/report_", "FailureImg/report_"+str(random.randint(1,101)))
        snappath = snappath+"/"+strP
        driver.get_screenshot_as_file(snappath)
        tlog = """
                      <tr row-id='""" + str(self.childid) + """' parent-id='""" + str(self.parentid) + """'>
                        <td><font color='red'>""" + log + """</font></td><td class="fail" id="fail" parentid='""" + str(
            self.parentid) + """'><img src="css/images/fail.png"/>&nbsp FAIL</td><td class="data">""" + str(
            time.strftime("%H:%M:%S")) + """</td>
                      </tr>
                      <tr row-id='""" + str(self.childid + 1) + """' parent-id='""" + str(self.childid) + """'>
                        <td colspan="3"><img src='FailureImages/""" + strP + """' width="25%" height="25%"/></td>
                      </tr>
                    """
        self.f.writelines(tlog)
        self.f.close()

    def close_report(self):
        self.f = open(self.filepath, "r+")
        data = self.f.read()
        data = data.replace("</table></div></body></html>", '')
        self.f.seek(0)
        self.f.truncate()
        self.f.writelines(data + "</table></div></body></html>")
        self.f.close()


class support_logger():

    def create_support(self, support_js):
        if not os.path.exists(support_js + "/css"):
            os.mkdir(support_js + "/css")
        support_js = support_js + "/css"

        f = open(support_js + "/jquery.tbltree.js", "a")
        tlog = """/*
 * jQuery tbletree Plugin 1.0.0
  * 
 * Copyright 2014, Gagik Sukiasyan
 * Licensed under the MIT licenses.
 */
(function($) {
	 $.widget( "ui.tbltree", {
      // default options
      options: {

		rowAttr: 'row-id',
		parentAttr: 'parent-id',
		treeColumn: 0,

		saveState: false,
		saveStateName: 'tbltree-state',
		saveStateMethod: 'cookie',
		initState: 'collapsed',
		levelPicker: '',

		expanderTemplate: '<span class="tbltree-expander"></span>',
		levelPickerTemplate: '<div class="tbltree-level-pickers">\
								<span id="0" class="tbltree-level-item">[1]</span>&nbsp;\
								<span id="1" class="tbltree-level-item">[2]</span>&nbsp;\
								<span id="2" class="tbltree-level-item">[3]</span>&nbsp;\
								<span id="3" class="tbltree-level-item">[4]</span>&nbsp;\
							  </div>',
        indentTemplate: '<span class="tbltree-indent"></span>',
        expanderExpandedClass: 'tbltree-expander-expanded',
        expanderCollapsedClass: 'tbltree-expander-collapsed',


		count: {
			enabled: false,
			format: '<div class="tbltree-count-wrap">(<span class="tbltree-count"></span>)</div>',
			method: function(row) {
				// count every row
				return 1;
			},
			click: null
		},

        // callbacks
        change: null,
		expand: null,
		collapse: null,
		showlevel: null
      },

		 // the constructor
		_create: function() {
			var $this = this;
			this.element
			  .addClass( "jquery-tbltree" )

			if (this.options.levelPicker !== "" && $(this.options.levelPicker).length > 0) {
				this.pickers = $(this.options.levelPickerTemplate);
				this.pickers.find('.tbltree-level-item').click(function(){
					$this.showLevel($(this).attr('id'))
				})
				$(this.options.levelPicker).append(this.pickers);
			}
		},
		_init: function() {
			var $this = this;
			this.getRootNodes().each(function(){
				$this._initTree($(this));
			})
		},

		getID: function(row) {
			return row.attr(this.options.rowAttr);
		},
		getParentID: function(row) {
			return row.attr(this.options.parentAttr);
		},
		isExpanded: function(cell) {
            return cell.hasClass('tbltree-expanded');
        },
		isCollapsed: function(cell) {
            return cell.hasClass('tbltree-collapsed');
        },
		getRootNodes: function () {
			var nodes = this.element.find('tr['+this.options.rowAttr+']').not('tr['+this.options.parentAttr+']')
			return nodes
		},
		getRow: function(id) {
			return this.element.find('tr['+this.options.rowAttr+'="'+id+'"]');
		},

		saveState: function(row) {
            var $this = this;
            if ($this.options.saveState && $this.options.saveStateMethod === 'cookie') {

                var stateArrayString = $.cookie(this.options.saveStateName) || '';
                var stateArray = (stateArrayString === '' ? [] : stateArrayString.split(','));
                var nodeId = $this.getID(row);

                if ($this.isExpanded(row)) {
                    if ($.inArray(nodeId, stateArray) === -1) {
                        stateArray.push(nodeId);
                    }
                } else if ($this.isCollapsed(row)) {
                    if ($.inArray(nodeId, stateArray) !== -1) {
                        stateArray.splice($.inArray(nodeId, stateArray), 1);
                    }
                }
                $.cookie(this.options.saveStateName, stateArray.join(','));
            }
            return $this;
        },
		getState: function(row) {
            var $this = this;

            if ($this.options.saveState && $this.options.saveStateMethod === 'cookie') {
				var stateArrayString = $.cookie(this.options.saveStateName) || '';
                var stateArray = (stateArrayString === '' ? [] : stateArrayString.split(','));
                if ($.inArray($this.getID(row), stateArray) !== -1) {
                    return "expanded";
                } else {
					return "collapsed";
                }

            }
            return $this.options.initState;
        },

		toggle: function (row) {
			if (typeof(row) != "object") {
				row = this.getRow(row);
			} 
			if (this.isCollapsed(row)) {
				this.expand(row, 1);

			} else {
				this.collapse(row, 1);
			}
		},

		collapse: function(id, user) {
				var $this = this;

				if (typeof(id) === "object") {
					row_id = this.getID(id);
					row = id;
				} else {
					row_id = id;
					row = this.getRow(row_id);
				}


				var row_id = this.getID(row);	
				if (user) {
					this.render(row, 'collapsed');
					this.saveState(row);
					this._trigger("collapse", null, row);
					this._trigger("change", null, {type: 'collapsed', 'row': row});
				}

				this._getChildren(row_id).each(function(){
					$(this).hide();
					$this.collapse($(this), 0);
				})
		},
		expand: function(id, user) {
				var $this = this;

				if (typeof(id) === "object") {
					row_id = this.getID(id);
					row = id;
				} else {
					row_id = id;
					row = this.getRow(row_id);
				}

				var row_id = this.getID(row);	
				if (user) {
					this.render(row, 'expanded')
					this.saveState(row);
					this._trigger("expand", null, row);
					this._trigger("change", null, {type: 'expanded', 'row': row});
				} 

				this._getChildren(row_id).each(function(){
					if ( ! $this.isCollapsed($(this))) {
						$this.expand($(this), 0);
					}
					$(this).show();
				})
		},

		expandLevel: function(level) {
			var $this = this;
			$this.element.find('tr[level]').filter(function() {
			    return  $(this).attr("level") <= level;
			})
			.each(function(){
				$this.expand($(this), 1);
			})
		},

		collapseLevel: function(level) {
			var $this = this;
			$this.element.find('tr[level='+level+']').each(function(){
					$this.collapse($(this), 1);
			})

		},

		showLevel: function(level) {
			var $this = this;
			if (level > 0) {
				$this.expandLevel(level - 1);
			}
			$this.collapseLevel(level);
			this._trigger("showlevel", null, level);
		},

		render: function(row, state) {
			var $this = this;
			if (state == 'collapsed') {
				row.attr('tree-state', 'hidden')
				row.removeClass('tbltree-expanded');
				row.addClass('tbltree-collapsed');
			} else {
				row.attr('tree-state', 'shown')
				row.removeClass('tbltree-collapsed');
				row.addClass('tbltree-expanded');
			}
			this._renderExpander(row);
        },

		_getChildren: function (id) {
			if (typeof(id) === "object") {
				id = this.getID(id);	
			}
			return this.element.find('tr['+this.options.parentAttr+'="'+id+'"]');
		},

		getTreeCell: function (row) {
			return $(row.find('td').get(this.options.treeColumn));
		},

		isLeaf: function(row) {
			if (row.attr('is-leaf') == "true") {
				return true;
			}
			return false;
		},

		_initExpander: function(root) {
            var $this = this;

           var cell = this.getTreeCell(root);

            var tpl = $(this.options.expanderTemplate);
            var expander = root.find('.tbltree-expander');
            if (expander) {
                expander.remove();
            }
			tpl.prependTo(cell)

			tpl.click(function() {
				$this.toggle(root)
            });

        },
		_renderExpander: function(cell) {
			if (cell.attr('is-leaf') == "true") {
				return;
			}
			var expander = cell.find('.tbltree-expander');
			if (expander.length) {
                if (!this.isCollapsed(cell)) {
                    expander.removeClass(this.options.expanderCollapsedClass);
                    expander.addClass(this.options.expanderExpandedClass);
                } else {
					expander.removeClass(this.options.expanderExpandedClass);
                    expander.addClass(this.options.expanderCollapsedClass);
                }
			} else {
                this._initExpander(cell);
				this._renderExpander(cell);
            }
        },

        _initIndent: function(cell, level) {
            cell.find('.tbltree-indent').remove();			
			var $indent = $(this.options.indentTemplate);
			$indent.css('width', (level * 16));
			$indent.insertBefore(cell.find('.tbltree-expander'));
        },

		_initTree: function(row, parent, level) {
			var $this = this;
			level = (level == undefined) ? 0: level;

			var children = this._getChildren(row);

			$this._initExpander(row);
			$this._initIndent(row, level)
			row.attr('level', level);
			row.attr('is-leaf', (children.length == 0));

			$this.render(row, this.getState(row));

			if (parent !== undefined && parent.attr('tree-state') == 'hidden') {
				row.hide();
				row.attr('tree-state', 'hidden');
			} else {
				row.show();
			}
			if (children.length != 0) {
				var count = $this._getCount(row);
				$.each(children, function(i, tree){
					$this._initTree($(tree), row, level+1);
					count += $this._getCount($(tree));
				})

				$this._setCount(row, count);
			} 
		},

		_getCount: function(row) {
			if (!this.options.count.enabled) {
				return 0;
			}

			var count = row.attr('count');
			if (count != undefined) {
				return parseInt(count);
			}
			count = 0;
			if (typeof(this.options.count.method) === "function") {
				count += parseInt(this.options.count.method(row));
			}
			return count;
		},

		_setCount: function(row, count) {		
			if (!this.options.count.enabled) {
				return 0;
			}

			var $this = this;
			if (typeof(this.options.count.format) === "function") {
				this.options.count.format(row, count);
			} else {
				var elem = $(this.options.count.format);
				elem.find('.tbltree-count').text(count)
				elem.appendTo(this.getTreeCell(row))

				if (typeof(this.options.count.click) === "function") {
					elem.css('cursor', 'pointer').click(function(e) {
						$this.options.count.click(e, row, count)
					} )
				}
			}
			row.attr('count', count);
		},

      // events bound via _on are removed automatically
      // revert other modifications here
      _destroy: function() {
        this.element
          .removeClass( "jquery-tbltree" )
          .enableSelection()

		this.pickers.remove();  
      },

      // _setOptions is called with a hash of all options that are changing
      // always refresh when changing options
      _setOptions: function() {
        // _super and _superApply handle keeping the right this-context
        this._superApply( arguments );
      },

      // _setOption is called for each individual option that is changing
      _setOption: function( key, value ) {
        // prevent invalid color values
        this._super( key, value );
      }
    });

})(jQuery);"""
        f.writelines(tlog)
        f.close()
        f = open(support_js + "/jquery.cookie.js", "a")
        tlog = """/*!
             * jQuery Cookie Plugin v1.3.1
             * https://github.com/carhartl/jquery-cookie
             *
             * Copyright 2013 Klaus Hartl
             * Released under the MIT license
             */
            (function (factory) {
                if (typeof define === 'function' && define.amd) {
                    // AMD. Register as anonymous module.
                    define(['jquery'], factory);
                } else {
                    // Browser globals.
                    factory(jQuery);
                }
            }(function ($) {

                var pluses = /\+/g;

                function decode(s) {
                    if (config.raw) {
                        return s;
                    }
                    return decodeURIComponent(s.replace(pluses, ' '));
                }

                function decodeAndParse(s) {
                    if (s.indexOf('"') === 0) {
                        // This is a quoted cookie as according to RFC2068, unescape...
                        s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
                    }

                    s = decode(s);

                    try {
                        return config.json ? JSON.parse(s) : s;
                    } catch(e) {}
                }

                var config = $.cookie = function (key, value, options) {

                    // Write
                    if (value !== undefined) {
                        options = $.extend({}, config.defaults, options);

                        if (typeof options.expires === 'number') {
                            var days = options.expires, t = options.expires = new Date();
                            t.setDate(t.getDate() + days);
                        }

                        value = config.json ? JSON.stringify(value) : String(value);

                        return (document.cookie = [
                            config.raw ? key : encodeURIComponent(key),
                            '=',
                            config.raw ? value : encodeURIComponent(value),
                            options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
                            options.path    ? '; path=' + options.path : '',
                            options.domain  ? '; domain=' + options.domain : '',
                            options.secure  ? '; secure' : ''
                        ].join(''));
                    }

                    // Read
                    var cookies = document.cookie.split('; ');
                    var result = key ? undefined : {};
                    for (var i = 0, l = cookies.length; i < l; i++) {
                        var parts = cookies[i].split('=');
                        var name = decode(parts.shift());
                        var cookie = parts.join('=');

                        if (key && key === name) {
                            result = decodeAndParse(cookie);
                            break;
                        }

                        if (!key) {
                            result[name] = decodeAndParse(cookie);
                        }
                    }

                    return result;
                };

                config.defaults = {};

                $.removeCookie = function (key, options) {
                    if ($.cookie(key) !== undefined) {
                        // Must not alter options, thus extending a fresh object...
                        $.cookie(key, '', $.extend({}, options, { expires: -1 }));
                        return true;
                    }
                    return false;
                };

            }));"""
        f.writelines(tlog)
        f.close()
        f = open(support_js + "/script.js", "a")
        tlog = """(function($) {
        $(document).ready(function(){

          // putting lines by the pre blocks
          $("pre").each(function(){
            var pre = $(this).text().split("\n");
            var lines = new Array(pre.length+1);
            for(var i = 0; i < pre.length; i++) {
              var wrap = Math.floor(pre[i].split("").length / 70)
              if (pre[i]==""&&i==pre.length-1) {
                lines.splice(i, 1);
              } else {
                lines[i] = i+1;
                for(var j = 0; j < wrap; j++) {
                  lines[i] += "\n";
                }
              }
            }
            $(this).before("<pre class='lines'>" + lines.join("\n") + "</pre>");
          });

          var headings = [];

          var collectHeaders = function(){
            headings.push({"top":$(this).offset().top - 15,"text":$(this).text()});
          }

          if($(".markdown-body h1").length > 1) $(".markdown-body h1").each(collectHeaders)
          else if($(".markdown-body h2").length > 1) $(".markdown-body h2").each(collectHeaders)
          else if($(".markdown-body h3").length > 1) $(".markdown-body h3").each(collectHeaders)

          $(window).scroll(function(){
            if(headings.length==0) return true;
            var scrolltop = $(window).scrollTop() || 0;
            if(headings[0] && scrolltop < headings[0].top) {
              $(".current-section").css({"opacity":0,"visibility":"hidden"});
              return false;
            }
            $(".current-section").css({"opacity":1,"visibility":"visible"});
            for(var i in headings) {
              if(scrolltop >= headings[i].top) {
                $(".current-section .name").text(headings[i].text);
              }
            }
          });

          $(".current-section a").click(function(){
            $(window).scrollTop(0);
            return false;
          })
        });
        })(jQuery)"""
        f.writelines(tlog)
        f.close()
        f = open(support_js + "/jquery.tbltree.css", "a")
        tlog = """.tbltree-indent {width:16px; height: 16px; display: inline-block; position: relative; border: 2;}

        .tbltree-expander {width:16px; height: 16px; display: inline-block; position: relative; cursor: pointer;}

        .tbltree-expander-expanded{background-image: url(images/collapse.png);}
        .tbltree-expander-collapsed{background-image: url(images/expand.png);}

        .tbltree-level-pickers {float: left;}
        .tbltree-level-pickers .tbltree-level-item {cursor: pointer;}
        .tbltree-count-wrap {
        	font-style: italic;
        	font-size: 10px;
        	float: right;
        }
        """
        f.writelines(tlog)
        f.close()

