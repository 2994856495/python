window.onload = function() {

  // UE or UES?
  var product  = getParam('prod') ? getParam('prod') : 'ue';
  var language = getParam('ln') ? getParam('ln') : 'en';
  var theme    = getParam('theme') ? getParam('theme') : '';
  var layout   = getParam('layout') ? getParam('layout') : '';
  var mode     = getParam('mode') ? getParam('mode') : '';
  var backup   = getParam('backup') ? getParam('backup') : '';
  var backupDir= getParam('backupdir') ? getParam('backupdir') : '';
  var tabs     = getParam('tabs') ? getParam('tabs') : '';
  var tabSize  = getParam('tabsize') ? getParam('tabsize') : '';

  /* ----------------------------------
      1) Localize + set product name
  ------------------------------------- */
  // Localize strings
  for (var str in langs) {
    var uid = 'l_' + str;
    var elems = document.querySelectorAll('.' + uid);

    for (var i = 0; i < elems.length; i++) {
      elems[i].innerHTML = langs[str][language];
    }
  }

  // Localize images
  var img_elems = document.querySelectorAll('.img_loc');
  for (var i = 0; i < img_elems.length; i++) {
    if (language !== 'en') {
      img_elems[i].src = img_elems[i].src.replace(/(\/[\w\d\s\-\_]+\.\w+$)/gi, '/' + language + '/' + "$1");
    }
  }

  // Set application name
  var productName = document.getElementById('productName');
  productName.innerHTML = conf_apps[product].appname;

  // Set default layout selection based on the app
  var layouts = ['Balanced', 'Lean', 'Clean', 'Multi-Window'];
  if (layout !== '') {
    for (i = 0; i < layouts.length; i++) {
      var element = document.getElementById(layouts[i]);
      if (element) {
        var cClass = element.className.replace("chosen", "");
        element.setAttribute('class', layout === layouts[i] ? cClass + ' chosen' : cClass);
      }
    }
  }

  // Set default theme selection based on the app
  var themes = ['Slate', 'Classic', 'Charcoal', 'Titanium'];
  if (theme !== '') {
    for (i = 0; i < themes.length; i++) {
      var element = document.getElementById(themes[i]);
      if (element) {
        element.className = element.className.replace("chosen", "");
        if (theme === themes[i]) {
          element.className += ' chosen';
          var DynCssAttr = element.getAttribute('data-css');
          if (DynCssAttr) {
            removeElement(element);
            var head = document.getElementsByTagName('head')[0];
            var s = document.createElement('link');
            s.setAttribute('rel', 'stylesheet');
            s.setAttribute('href', element.getAttribute('data-css') + '.css');
            s.setAttribute('id', 'CssDynAdd');
            head.appendChild(s);
          }
        }
      }
    }
  }

  // Set default mode selection based on the app
  var modes = ['ribbon', 'menus_toolbars', 'menus'];
  if (mode !== '') {
    for (i = 0; i < modes.length; i++) {
      var element = document.getElementById(modes[i]);
      if (element) {
        var cClass = element.className.replace("chosen", "");
        element.className = mode === modes[i] ? cClass + ' chosen' : cClass;
      }
    }
  }

  // Set settings based on the app
  if (tabs !== '') {
    var element = document.getElementById('s_tab_' + tabs);
    if (element) {
      element.checked = true;
    }
  }

  if (tabSize !== '') {
    var element = document.getElementById('s_tab_size');
    if (element) {
      element.value = tabSize;
    }
  }

  if (backup !== '') {
    var element = document.getElementById('s_bak_' + backup);
    if (element) {
      element.checked = true;
    }
  }

  if (backupDir !== '') {
    var element = document.getElementById('s_bak_2i');
    if (element) {
      element.value = backupDir;
    }
  }

  /* ----------------------------------
      2) Set up listeners for selector classes
  ------------------------------------- */

  // selectThings should contain all IDs of tables containing a user-selectable setting
  var selectThings = ["theme_select", "layout_select", "ribbon_select"];
  var classChoice = "select";
  var classAdd = "chosen";

  for (i = 0; i < selectThings.length; i++) {
    setUpListener(selectThings[i]);
  }

  function setUpListener(elemID) {
    var t = document.getElementById(elemID);
    var selectors = t.getElementsByClassName(classChoice);
    for (var i = 0; i < selectors.length; i++) {
      selectors[i].addEventListener('click', function() {
        var regex = new RegExp("(?:^|\\s)" + classAdd + "(?!\\S)", "g");
        for (var i = 0; i < selectors.length; i++) {
          selectors[i].className = selectors[i].className.replace(regex, '');
        }
        // now add it to clicked element - remember IE doesn't support event.target
        var evt = event.target || window.event.srcElement;
        evt.parentElement.className += " " + classAdd;
      });
    }
  }

  // Set up listener for on-the-fly CSS / theme switch
  var themeEls = document.getElementsByClassName('selectTheme');
  for (i = 0; i < themeEls.length; i++) {
    var cssAttr = themeEls[i].getAttribute('data-css');
    if (cssAttr) {
      var addCSS = cssAttr + ".css"
      themeEls[i].addEventListener('click', function() {
        removeElement('CssDynAdd')
        var head = document.getElementsByTagName('head')[0];
        var s = document.createElement('link');
        s.setAttribute('rel', 'stylesheet');
        s.setAttribute('href', this.getAttribute('data-css') + '.css');
        s.setAttribute('id', 'CssDynAdd');
        head.appendChild(s);
      });
    } else {
      // in this case, default style should be used,
      // so we must REMOVE any dynamically inserted style
      themeEls[i].addEventListener('click', function() {
		  removeElement('CssDynAdd')
      });
    }
  }

  /* -------- funcs -------------------- */

  // Adds CSS to end of <head>
  function removeElement(element) {
    var element = document.getElementById('CssDynAdd');
    if (element) element.parentNode.removeChild(element);
  }


  // Gets URL parameters
  function getParam(name) {
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||null
  }

  window.location.href = "#ONLOADCOMPLETE";
};

// Object with app names and properties
conf_apps = {

  ue: {
    appname: 'UltraEdit'
  },

  ues: {
    appname: 'UEStudio'
  },

  uep: {
    appname: 'UE Mobile'
  },

  uc: {
    appname: 'UltraCompare'
  },

  uf: {
    appname: 'UltraFinder'
  },

  us: {
    appname: 'UltraSentry'
  },

  ucp: {
    appname: 'UC Mobile'
  }
};