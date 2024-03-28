import './App.css'
import MainTable from './pro/MainTable'
// import GetPatiets from './pro/api/CoronaPatientDetails';
// import AddPatient from './pro/AddPatient';

function App() {
  return (
    <div className="App">
      <header className="App-header">
       <MainTable></MainTable> 
       {/* <GetPatiets></GetPatiets> */}
       {/* <AddPatient></AddPatient> */}
      </header>
    </div>
  );
}

export default App;
