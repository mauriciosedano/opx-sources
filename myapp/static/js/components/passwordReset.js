let passwordReset = new Vue({
    el: '#password-reset',
    delimitters: ['[[', ']]'],
    data: {
        email: '',
        reset: {
            password: ''
        }
    },
    methods: {
        verificacion(){

            let data = "email=" + this.email

            axios({
                url: '/auth/password-reset-verification/',
                method: 'POST',
                data: data,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                Swal.fire({
                    title: 'Éxito',
                    text: 'Revisa tu correo electrónico',
                    type: 'success'
                })
                .then(response => {

                    if(response.value)
                        location.href = '/';
                })
            })
            .catch(response => {

                Swal.fire({
                    title: 'Error',
                    text: 'La cuenta de correo proveida no existe en nuestro sistema',
                    type: 'error'
                });
            })
        },
        reestablecimiento(){

            let data = Object.keys(this.reset).map(key => {
                return key + "=" + this.reset[key];
            }).join('&');

            axios({
                url: '/auth/password-reset-done/',
                method: 'POST',
                data: data,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            })
            .then(response => {

                Swal.fire({
                    title: 'Exito',
                    text: 'La contraseña fue restablecida satisfactoriamente',
                    type: 'success'
                })
                .then(response => {

                    if(response.value)
                        location.href = "/";
                });
            })
            .catch(response => {

               Swal.fire({
                   title: 'Error',
                   text: 'Ocurrio un error. Por favor intenta de nuevo',
                   type: 'error'
               });
            });
        }
    }
})