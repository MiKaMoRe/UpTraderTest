const path = window.location.pathname
const active_dirs = path.substring(1).split('/')

document
  .querySelectorAll('.tree-menu')
  .forEach(menu => {
    menu
      .querySelectorAll('li')
      .forEach(elem => {
        parentId = elem.getAttribute('data-parent-id')
        if (parentId != null) {
          menu.querySelector(`li[data-id="${parentId}"] ul`).append(elem)
        }
        if (elem.getAttribute('data-is-active')){
          elem.querySelector('ul').classList.add('active')
        }
      })
  })