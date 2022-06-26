let theme = localStorage.getItem('data-theme');

if (theme == null) {
    document.documentElement.setAttribute('data-theme', 'dark');
}
else {
    document.documentElement.setAttribute('data-theme', theme);
}

function switchTheme() {
    let select = document.getElementById('theme');
    let value = select.options[select.selectedIndex].value;
    document.documentElement.setAttribute('data-theme', value);
    localStorage.setItem('data-theme', value);
}