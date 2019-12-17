var expanded = [];

function unexpand(name) {
    expanded = expanded.filter(function(e) {return e != name;});
    sessionStorage.setItem('expanded', expanded.join(','));
}

function getExpandedCookie() {
    var v = sessionStorage.getItem("expanded");
    if (v) {
        expanded = v.split(',').filter(function(e){return e != "";});
    } else {
        expanded = [];
    }
}

function showItem(item) {
    item.className = "nav_sect_inner";
    expanded.push(item.id);
    sessionStorage.setItem("expanded", expanded.join(","));
}

function hideItem(item) {
    //item.style.display = "none";
    item.className = "nav_sect_inner hidden";
    unexpand(item.id);
}

function expandExpanded() {
    for (var i = 0; i < expanded.length; i++) {
        document.getElementById(expanded[i]).className = "nav_sect_inner";
    }
}

function showNav(path) {
    var items = path.split("/");
    var i;
    for (i = 0; i < items.length - 1; i++) {
        d = document.getElementById(items.slice(0, i + 1).join("/"));
        showItem(d);
    }
}

var coll = document.getElementsByClassName("nav_sect");
var i;
for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        var content = this.nextElementSibling;
        if (content.className === "nav_sect_inner") {
            hideItem(content);
        } else {
            showItem(content);
        }
    });
}

getExpandedCookie();
expandExpanded();

for (const impl_collapsed of document.getElementsByClassName('impl_collapsed')) {
    const impl_args = impl_collapsed.getElementsByClassName('impl_arg');
    if (impl_args.length > 0) {
        impl_args[0].addEventListener('click', () =>
            impl_collapsed.classList.remove('impl_collapsed'));
    }
}