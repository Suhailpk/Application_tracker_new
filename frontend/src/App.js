import "./App.css";
import { BrowserRouter, Navigate, Routes, Route } from "react-router-dom";
import Login from "./components/pages/Login";
import SignUp from "./components/pages/SignUp";
import Navbar from "./components/pages/Navbar";
import Home from "./components/pages/Home";
import CompanyIntro from "./components/pages/CompanyIntro";
import ProtectedRouter from "./components/pages/ProtectedRouter";
import ApplicationDetail from "./components/pages/ApplicationDetail";
import AddApplication from "./components/pages/AddApplication";
import EditApplication from "./components/pages/EditApplication";
import DeleteApplication from "./components/pages/DeleteApplication";

function App() {

  const Logout = ()=>{
    localStorage.clear()
    return <Navigate to={'/login'}/>
  }
  
  function RegisterAndLogout(){
    localStorage.clear()
    return <SignUp />
  }

  return (

      <Routes>
        <Route path="/comapny_intro" element={<CompanyIntro />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/signup" element={<SignUp />} />
        <Route
          path="/"
          element={
            <ProtectedRouter>
              <Navbar />
            </ProtectedRouter>
          }
        />
        <Route path="/application_detail" element={
          <ProtectedRouter>
            <ApplicationDetail />
          </ProtectedRouter>
        }/>
        <Route path="/add_application" element={
          <ProtectedRouter>
            <AddApplication />
          </ProtectedRouter>
        }/>
        <Route path="/application_detail/edit/:id" element={
          <ProtectedRouter>
            <EditApplication />
          </ProtectedRouter>
        }/>
        <Route path="/application_detail/delete/:id" element={
          <ProtectedRouter>
            <DeleteApplication />
          </ProtectedRouter>
        }/>
      </Routes>
   
 );
 
}


export default App;
