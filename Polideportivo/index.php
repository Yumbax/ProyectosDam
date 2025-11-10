<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Archivo donde guardamos las reservas
$archivo = 'reservas.json';

// Leer reservas existentes
$reservas = file_exists($archivo) ? json_decode(file_get_contents($archivo), true) : [];

// Array de pistas
$pistas = [
    ["nombre" => "Campo de Fútbol 11", "deporte" => "Fútbol"],
    ["nombre" => "Cancha de Baloncesto", "deporte" => "Baloncesto"],
    ["nombre" => "Pista de Atletismo", "deporte" => "Atletismo"],
    ["nombre" => "Cancha de Vóley", "deporte" => "Vóley"],
    ["nombre" => "Pista de Pádel 1", "deporte" => "Pádel"],
    ["nombre" => "Pista de Tenis 1", "deporte" => "Tenis"]
];

// Procesar nueva reserva
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nueva = [
        "id_reserva" => count($reservas) + 1,
        "nombre_usuario" => $_POST['nombre'],
        "pista" => $_POST['pista'],
        "deporte" => $_POST['deporte'],
        "fecha" => $_POST['fecha'],
        "hora" => $_POST['hora']
    ];
    $reservas[] = $nueva;
    file_put_contents($archivo, json_encode($reservas, JSON_PRETTY_PRINT));
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reservas Polideportivo</title>
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <h1>Reservas del Polideportivo</h1>

    <section class="formulario">
        <h2>Hacer una reserva</h2>
        <form method="POST">
            <input type="text" name="nombre" placeholder="Tu nombre" required>
            <select name="pista" required>
                <option value="">Selecciona pista</option>
                <?php foreach($pistas as $p): ?>
                    <option value="<?= $p['nombre'] ?>" data-deporte="<?= $p['deporte'] ?>"><?= $p['nombre'] ?> (<?= $p['deporte'] ?>)</option>
                <?php endforeach; ?>
            </select>
            <input type="hidden" name="deporte" id="deporte_input">
            <input type="date" name="fecha" required>
            <input type="time" name="hora" required>
            <button type="submit">Reservar</button>
        </form>
    </section>

    <section class="tabla">
        <h2>Reservas actuales</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Usuario</th>
                <th>Pista</th>
                <th>Deporte</th>
                <th>Fecha</th>
                <th>Hora</th>
            </tr>
            <?php if (!empty($reservas)): ?>
                <?php foreach($reservas as $r): ?>
                    <tr>
                        <td><?= $r['id_reserva'] ?></td>
                        <td><?= $r['nombre_usuario'] ?></td>
                        <td><?= $r['pista'] ?></td>
                        <td><?= $r['deporte'] ?></td>
                        <td><?= $r['fecha'] ?></td>
                        <td><?= $r['hora'] ?></td>
                    </tr>
                <?php endforeach; ?>
            <?php else: ?>
                <tr><td colspan="6">No hay reservas todavía</td></tr>
            <?php endif; ?>
        </table>
    </section>

    <script>
        const select = document.querySelector('select[name="pista"]');
        const inputDeporte = document.getElementById('deporte_input');
        select.addEventListener('change', () => {
            inputDeporte.value = select.options[select.selectedIndex].dataset.deporte;
        });
    </script>
</body>
</html>
