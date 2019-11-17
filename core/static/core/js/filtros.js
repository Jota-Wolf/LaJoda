$(document).ready(function() {

    var baseUrlcasas = 'http://localhost:8000/casas/';
    var fil_cas_tipo_contacto = $('#fil_cas_tipo_contacto');
    var fil_cas_habitaciones = $('#fil_cas_habitaciones');

    var baseUrldeptos = 'http://localhost:8000/departamento/';
    var fil_depto_tipo_contacto = $('#fil_depto_tipo_contacto');
    var fil_depto_habitaciones = $('#fil_depto_habitaciones');

    var baseUrlterres = 'http://localhost:8000/terrenos/';
    var fil_terr_tipo_contacto = $('#fil_terr_tipo_contacto');
    var fil_terr_ciudad = $('#fil_terr_ciudad');

    $(fil_cas_tipo_contacto).change(function() {
        var fil_cas_tipo_contacto = $(this).val();
        window.location.href = baseUrlcasas + '?filtro_contacto=' + fil_cas_tipo_contacto;
    });

    $(fil_cas_habitaciones).change(function() {
        var fil_cas_habitaciones = $(this).val();
        window.location.href = baseUrlcasas + '?filtro_habitaciones=' + fil_cas_habitaciones;
    });

    $(fil_depto_tipo_contacto).change(function() {
        var fil_depto_tipo_contacto = $(this).val();
        window.location.href = baseUrldeptos + '?filtro_contacto=' + fil_depto_tipo_contacto;
    });

    $(fil_depto_habitaciones).change(function() {
        var fil_depto_habitaciones = $(this).val();
        window.location.href = baseUrldeptos + '?filtro_habitaciones=' + fil_depto_habitaciones;
    });

    $(fil_terr_tipo_contacto).change(function() {
        var fil_terr_tipo_contacto = $(this).val();
        window.location.href = baseUrlterres + '?filtro_contacto=' + fil_terr_tipo_contacto;
    });

    $(fil_terr_ciudad).change(function() {
        var fil_terr_ciudad = $(this).val();
        window.location.href = baseUrlterres + '?filtro_ciudad=' + fil_terr_ciudad;
    });

});