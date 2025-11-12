let torneos = [];

// Cargar desde localStorage al iniciar
window.onload = function() {
    const datosGuardados = localStorage.getItem('torneos');
    if (datosGuardados) {
        torneos = JSON.parse(datosGuardados);
        actualizarLista();
    }
};

function guardarDatos() {
    localStorage.setItem('torneos', JSON.stringify(torneos));
}

function crearTorneo() {
    const nombre = document.getElementById('nombreTorneo').value.trim();
    if (nombre === "") {
        alert("Ingresa un nombre para el torneo");
        return;
    }

    const torneo = { nombre: nombre, equipos: [] };
    torneos.push(torneo);
    guardarDatos();
    actualizarLista();
    document.getElementById('nombreTorneo').value = "";
}

function inscribirEquipo() {
    const select = document.getElementById('torneoSelect');
    const equipo = document.getElementById('nombreEquipo').value.trim();
    if (select.value === "" || equipo === "") {
        alert("Selecciona un torneo e ingresa el nombre del equipo");
        return;
    }

    const torneo = torneos.find(t => t.nombre === select.value);
    torneo.equipos.push(equipo);
    guardarDatos();
    actualizarLista();
    document.getElementById('nombreEquipo').value = "";
}

function actualizarLista() {
    const container = document.getElementById('listaTorneos');
    const select = document.getElementById('torneoSelect');

    container.innerHTML = "";
    select.innerHTML = "<option value=''>--Selecciona torneo--</option>";

    torneos.forEach(torneo => {
        const card = document.createElement('div');
        card.className = "torneo-card";

        const h3 = document.createElement('h3');
        h3.textContent = torneo.nombre;
        card.appendChild(h3);

        const p = document.createElement('p');
        p.textContent = `Equipos inscritos: ${torneo.equipos.length}`;
        card.appendChild(p);

        const ul = document.createElement('ul');
        torneo.equipos.forEach(e => {
            const li = document.createElement('li');
            li.textContent = e;
            ul.appendChild(li);
        });
        card.appendChild(ul);

        container.appendChild(card);

        const option = document.createElement('option');
        option.value = torneo.nombre;
        option.textContent = torneo.nombre;
        select.appendChild(option);
    });
}
