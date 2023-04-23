const axios = require('axios')
const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000'
})
const user = {
    state: {
        users: [], //all users
        uid: null,
        bits_id: null,
        created: null,
        full_name: null,
        karma: null,
        u_name: null,
        pwd: null
    },
    getters: {
        getUser: (state) => {
            const userObj = {
                uid: state.uid,
                bits_id: state.bits_id,
                created: state.created,
                full_name: state.full_name,
                karma: state.karma,
                u_name: state.u_name,
                pwd: state.pwd
            }
            return userObj
        },

        getUserById: (state) => (id) => {
            let usr;
            for (let i in state.users) {
                console.log(id)
                if (state.users[i].id == id) {
                    usr = state.users[i]
                    console.log('Match User: ', state.users[i])
                }
            }
            return usr
        }
    },

    mutations: {
        setUser(state, payload) {
            state.uid = payload.id;
            state.bits_id = payload.bits_id;
            state.created = payload.created;
            state.full_name = payload.full_name;
            state.karma = payload.karma;
            state.u_name = payload.u_name;
            state.pwd = payload.pwd;
        },
        setUsers(state, payload) {
            state.users = payload
            console.log(payload)
        }
    },

    actions: {
        async GetUsers(context) {
            let res = await axiosInstance.get('/user')
            if (res.status === 200) {
                context.commit('setUsers', res.data)
            } else {
                console.log('Error :', res.data)
                context.commit('ShowError', res.data)
            }
        },

        async SignUpUser(context, formData) { //sign up
            console.log(formData)
            let res = await axiosInstance.post('/user',
                {
                    'bits_id': formData.bits_id,
                    'email': formData.email,
                    'full_name': formData.full_name,
                    'u_name': formData.u_name,
                    'pwd': formData.pwd
                })

            if (res.status === 200) {
                console.log(res.data)
                res.data.pwd = formData.pwd
                context.commit('setUser', res.data)
                context.commit('setLogIn')
            } else {
                console.log(res.data)
                context.dispatch('ShowError', res.data)
            }
        },

        async LogInUser({ commit, state, dispatch }, formData) {
            let possibleUser = null;
            for (let usr in state.users) {
                if (state.users[usr].u_name == formData.u_name) possibleUser = state.users[usr];
            }
            if (possibleUser) {
                let res = await axiosInstance.get('/user/' + possibleUser.id)
                if (res.status === 200) {
                    console.log('Login Response:', res.data)
                    if (res.data.pwd == formData.pwd) {
                        commit('setUser', res.data)
                        commit('setLogIn')
                    } else {
                        console.log('Incorrect username / password')
                        dispatch('ShowError', 'Incorrect username / password')
                    }
                } else {
                    console.log(res.data)
                    dispatch('ShowError', res.data)
                }
            } else {
                console.log('User does not exist')
                dispatch('ShowError', "User doesn't exist")
            }
        }
    }
}

export default user