import {Routes,Route} from 'react-router-dom'
import './App.css';
import {useState} from 'react'
import LoginPage from "./components/LoginPage"
function App() {
  const[currentUser,setCurrentUser] = useState({})
  return (
    <div className="App">
      "hello world"
      <LoginPage />
    </div>
  );
}

export default App;
