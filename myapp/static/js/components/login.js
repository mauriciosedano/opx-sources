let login = new Vue({
    delimiters: ['[[', ']]'],
    el: '#login',
    data: {
        loginInfo: {}
    },
    methods: {
        login(){

            if(!this.loginInfo.hasOwnProperty('username') || !this.loginInfo.hasOwnProperty('password')){

                Swal.fire({
                    title: 'Error',
                    text: 'Por favor diligencia toda la información',
                    type: 'error'
                });

            } else{

                let queryString = Object.keys(this.loginInfo).map(key => {

                    return key + '=' + this.loginInfo[key]
                })
                .join('&');

                axios({
                    method: 'post',
                    url: '/login/',
                    data: queryString,
                    headers: {
                        'Content-type': 'application/x-www-form-urlencoded'
                    }
                })
                .then(response => {

                    sessionStorage.setItem('userinfo', JSON.stringify(response.data));
                    location.href = '/proyectos';
                })
                .catch(error => {

                    Swal.fire({
                        title: 'Error',
                        text: 'Usuario y/o contraseña incorrecto(s)',
                        type: 'error'
                    });
                });
            }
        }
    }
})