import PatientItems from "./PatientItems";
import Popup from 'reactjs-popup';
import 'reactjs-popup/dist/index.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BASE_URL } from "./config";
import EditPatientForm from "./EditPatientForm";
import AddPatientForm from "./AddPatientForm";


function MainTable(params) {

    const [data, setData] = useState([]);
    const [editPatientData, setEditPatientData] = useState(null);
    const [showEditForm, setShowEditForm] = useState(false);
    const [showAddForm, setShowAddForm] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            try {
                await axios.get(`${BASE_URL}/corona_patient_controller/get_all`)
                    .then(response => {
                        setData(response.data);
                    });
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };
        fetchData()
    }, []);

    const fetchData = async () => {
        try {
            await axios.get(`${BASE_URL}/corona_patient_controller/get_all`)
                .then(response => {
                    setData(response.data);
                });
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    // const addPatient = async (newPatientData) => {
    //     try {
    //         await axios.post(`${BASE_URL}/add_patient`, newPatientData)
    //             .then(response => {
    //                 console.log('Patient added successfully:', response.data);
    //                 fetchData();
    //             })
    //     } catch (error) {
    //         console.error('Error adding patient:', error);
    //     };
    // };


    const deletePatient = async (id) => {
        try {
            await axios.delete(`${BASE_URL}/corona_patient_controller/delete_patient/${id}`)
                .then(response => {
                    console.log('Patient deleted successfully:', response.data);
                    fetchData();
                })
        } catch (error) {
            console.error('Error deleting patient:', error);
        };
    };

    const handleEditClick = (patientData) => {
        setEditPatientData(patientData);
        setShowEditForm(true);
    };

    const handleCloseEditForm = () => {
        setShowEditForm(false);
        fetchData();
    };
    const handleAddClick = () => {
        setShowAddForm(true);
    };

    const handleCloseAddForm = () => {
        setShowAddForm(false);
        fetchData();
    };


    return (
        <div className="App">
            <h2>Corona Patient Details</h2>
            <table>
                <thead>
                    <tr>
                        <th>  מועד החלמה  </th>
                        <th>  מועד תוצאה חיובית  </th>
                        <th>  חיסוני קורונה  </th>
                        <th>  מספר זהות  </th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((val, key) => {
                        return (
                            <tr key={key}>
                                {/* <input
                                    name="recovery"
                                    type="date"
                                    value={val.recovery}
                                    onChange={(event) => editPatient(event, key)}
                                /> */}
                                <td>{val.recovery} </td>
                                <td>{val.positive} </td>
                                <td>
                                    <ul>
                                        {val.corona_vaccines.map((vaccine, index) => (
                                            <li key={index}>
                                                Date: {vaccine.date}, Manufacturer: {vaccine.manufacturer}
                                            </li>
                                        ))}
                                    </ul>
                                </td>
                                <td>
                                    <Popup trigger=
                                        {<button> {val.id} </button>}
                                        modal nested  >
                                        {
                                            close => (
                                                <div className='modal'>
                                                    <div className='content'>
                                                        <PatientItems id={val.id}></PatientItems>
                                                    </div>
                                                    <div>
                                                        <button onClick=
                                                            {() => close()}>
                                                            Close
                                                        </button>
                                                    </div>
                                                </div>
                                            )
                                        }
                                    </Popup>
                                </td>
                                <td>
                                    <button onClick={() => deletePatient(val.id)}>🗑️</button>
                                </td>
                                <td>
                                    <button onClick={() => handleEditClick(val)}>✏️</button>
                                </td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
            <button onClick={handleAddClick}>להוספת חבר חדש בקופת החולים</button>
            {showEditForm && (
                <EditPatientForm patientData={editPatientData} onClose={handleCloseEditForm} />
            )}
            {showAddForm && (
                <AddPatientForm onClose={handleCloseAddForm} />
            )}
        </div>
    )
} export default MainTable;