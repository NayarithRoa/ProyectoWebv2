(async () => {

    const { value: rol } = await Swal.fire({
        title: 'Rol',
        input: 'select',
        inputOptions: {
            paciente: 'Paciente',
            cuidadador: 'Cuidador',
            personalMedico: 'Personal médico'
          
        },
        inputPlaceholder: 'Seleccione un rol',
        showCancelButton: true
      })
      
      if (rol) {
        //window.location = "../registroDatosBasicos.html";
        //window.location.href = "https://mapsplatform.google.com/";
        window.location.href = "solicitarDatosBasicos";
        Swal.fire(`You selected: ${rol}`)
      }
    })()