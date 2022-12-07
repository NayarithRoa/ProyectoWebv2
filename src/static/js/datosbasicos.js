function mostrardetalleCaja(aspecto) {

    switch(aspecto) {
        case 1:  
            var encabezado = document.getElementById("cajaencabezado");
            var detalle = document.getElementById("cajadetalle");
            break;
    
        case 2:  
            var encabezado = document.getElementById("cajaencabezado1");
            var detalle = document.getElementById("cajadetalle1");
            break;
    
        case 3:
            var encabezado = document.getElementById("cajaencabezado2");
            var detalle = document.getElementById("cajadetalle2");
            break;
        case 4:
            var encabezado = document.getElementById("cajaencabezado3");
            var detalle = document.getElementById("cajadetalle3");
            break;
        case 5:
            var encabezado = document.getElementById("cajaencabezado4");
            var detalle = document.getElementById("cajadetalle4");
            break;
        case 6:
            var encabezado = document.getElementById("cajaencabezado5");
            var detalle = document.getElementById("cajadetalle5");
            break;
        case 7:
            var encabezado = document.getElementById("cajaencabezado6");
            var detalle = document.getElementById("cajadetalle6");
            break;
        case 8:
            var encabezado = document.getElementById("cajaencabezado7");
            var detalle = document.getElementById("cajadetalle7");
            break;
        case 9:
            var encabezado = document.getElementById("cajaencabezado8");
            var detalle = document.getElementById("cajadetalle8");
            break;
        case 10:
            var encabezado = document.getElementById("cajaencabezado9");
            var detalle = document.getElementById("cajadetalle9");
            break;
    
        default:
            // body of default
    }
    if (encabezado.style.display === "none") {
        encabezado.style.display = "block";
        detalle.style.display = "none";
        encabezado.classList.add('magictime', 'puffIn')
    } else {
        encabezado.classList.add('magictime', 'puffIn')
        encabezado.style.display = "none";
        detalle.style.display = "block";
    }
  }

