$(document).ready(function() {

    var baseUrlcasas = 'http://localhost:8000/casas/';
    var fil_cas_tipo_contacto = $('#fil_cas_tipo_contacto');

    var baseUrldeptos = 'http://localhost:8000/departamento/';
    var fil_depto_tipo_contacto = $('#fil_depto_tipo_contacto');

    var baseUrlterres = 'http://localhost:8000/terrenos/';
    var fil_terr_tipo_contacto = $('#fil_terr_tipo_contacto');

    $(fil_cas_tipo_contacto).change(function() {
        var fil_cas_tipo_contacto = $(this).val();
        window.location.href = baseUrlcasas + '?filter=' + fil_cas_tipo_contacto;
    });

    $(fil_depto_tipo_contacto).change(function() {
        var fil_depto_tipo_contacto = $(this).val();
        window.location.href = baseUrldeptos + '?filter=' + fil_depto_tipo_contacto;
    });

    $(fil_terr_tipo_contacto).change(function() {
        var fil_terr_tipo_contacto = $(this).val();
        window.location.href = baseUrlterres + '?filter=' + fil_terr_tipo_contacto;
    });

});