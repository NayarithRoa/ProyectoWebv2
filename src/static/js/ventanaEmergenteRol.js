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
        showCancelButton: true,
        inputValidator: (value) => {
          return new Promise((resolve) => {
            if (value === 'Paciente') {
              resolve()
            }
          })
        }
      })
      
      if (rol) {
        Swal.fire(`You selected: ${rol}`)
      }
    })()