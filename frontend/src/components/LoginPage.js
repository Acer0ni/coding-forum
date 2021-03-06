import {useState} from 'react'
import getCookie from '../csrf';


function LoginPage(props) {
    const [credentials,setCredentials ] = useState({
        username:"username",
        password:"password"
    })
  const handleLogin = (e) => {
    let csrfToken = getCookie("csrftoken")
    e.preventDefault()
    fetch('/api/auth/login',{
      method:'POST',
      credentials: 'include',
      headers: {
        'X-CSRFToken':csrfToken,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username:credentials.username,
        password: credentials.password
      }),
    })
    .then((res)=> res.json())
    .then((data) => console.log(data))
  };
  const handleChange= (e) =>{
      const value = e.target.value
      const name = e.target.name
      const copy = Object.assign({},credentials)

      copy[name] = value
      setCredentials(copy)
  }


  return (
    <div>
      <h2>Please enter your username and and password to login</h2>
      <form onSubmit={() => {
          handleLogin();
        }}
      >
        <input value = {credentials.username} onChange={handleChange} type="text" name = "username"></input>
        <input value = {credentials.password} onChange={handleChange} type="password"name = "password"></input>
        <button onClick = {handleLogin} >login</button>
      </form>
    </div>
  );
}
export default LoginPage