let theme=localStorage.getItem("data-theme");function switchTheme(){let e=document.getElementById("theme"),t=e.options[e.selectedIndex].value;document.documentElement.setAttribute("data-theme",t),localStorage.setItem("data-theme",t)}null==theme?document.documentElement.setAttribute("data-theme","dark"):document.documentElement.setAttribute("data-theme",theme);