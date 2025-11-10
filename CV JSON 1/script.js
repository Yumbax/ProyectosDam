fetch('curriculum.json')
    .then(response => response.json())
    .then(data => {
        // Datos personales
        const datosPersonales = document.getElementById('datos-personales');
        datosPersonales.innerHTML = `
            <h1>${data.datos_personales.nombre}</h1>
            <p><a href="mailto:${data.datos_personales.email}">${data.datos_personales.email}</a> | ${data.datos_personales.telefono}</p>
        `;

        // Perfil
        document.getElementById('perfil-texto').textContent = data.datos_personales.perfil;

        // Formación
        const listaFormacion = document.getElementById('lista-formacion');
        data.formacion.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.titulo} - ${item.centro} (${item.anio_inicio} - ${item.anio_fin})`;
            listaFormacion.appendChild(li);
        });

        // Experiencia
        const listaExperiencia = document.getElementById('lista-experiencia');
        data.experiencia_profesional.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `<strong>${item.puesto}</strong> – ${item.empresas.join(', ')} (${item.periodo})<p>${item.descripcion}</p>`;
            listaExperiencia.appendChild(li);
        });

        // Idiomas
        const listaIdiomas = document.getElementById('lista-idiomas');
        data.idiomas.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.idioma} – ${item.nivel}`;
            listaIdiomas.appendChild(li);
        });

        // Vehículos
        const listaVehiculos = document.getElementById('lista-vehiculos');
        const liVeh = document.createElement('li');
        liVeh.textContent = `Carnet: ${data.vehiculos.carnet} | Vehículo propio: ${data.vehiculos.vehiculo_propio ? 'Sí' : 'No'}`;
        listaVehiculos.appendChild(liVeh);

        // Aficiones y hobbies
        const listaAficiones = document.getElementById('lista-aficiones');
        data.aficiones_y_hobbies.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            listaAficiones.appendChild(li);
        });

        // Habilidades
        const listaHabilidades = document.getElementById('lista-habilidades');
        data.habilidades.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item;
            listaHabilidades.appendChild(li);
        });

    })
    .catch(error => console.error('Error al cargar el JSON:', error));
