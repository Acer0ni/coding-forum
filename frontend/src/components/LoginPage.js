import {useState} from 'react'



function LoginPage(props) {
    const [credentials,setCredentials ] = useState({
        username:"username",
        password:"password"
    })
  const handleLogin = (e) => {
    e.preventDefault()
      console.log(`username,${credentials.username},password,${credentials.password}`)

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
        <input value = {credentials.password} onChange={handleChange} type="text"name = "password"></input>
        <button onClick = {handleLogin} ></button>
      </form>
    </div>
  );
}
export default LoginPage