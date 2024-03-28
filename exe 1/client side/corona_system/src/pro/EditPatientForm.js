import React, { useState } from 'react';
import axios from 'axios';
import { BASE_URL } from './config';

function EditPatientForm({ patientData, onClose }) {
    const [editedPatient, setEditedPatient] = useState(patientData);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setEditedPatient({ ...editedPatient, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            console.log(patientData.id);
            await axios.put(`${BASE_URL}/corona_patient_controller/edit_patient/${patientData.id}`, editedPatient, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            onClose(); 
        } catch (error) {
            console.error('Error editing patient:', error);
        }
    };

    return (
        <div className="edit-patient-form">
            <h2>Edit Patient</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Recovery Date:
                    <input type="date" name="recovery" value={editedPatient.recovery} onChange={handleInputChange} />
                </label>
                <label>
                    Positive Date:
                    <input type="date" name="positive" value={editedPatient.positive} onChange={handleInputChange} />
                </label>
                {/* <label>
                    Recovery Date:
                    <input type="date" name="recovery" value={editedPatient.recovery} onChange={handleInputChange} />
                </label>
                <label>
                    Recovery Date:
                    <input type="date" name="recovery" value={editedPatient.recovery} onChange={handleInputChange} />
                </label>
                <label>
                    Recovery Date:
                    <input type="date" name="recovery" value={editedPatient.recovery} onChange={handleInputChange} />
                </label>
                <label>
                    Recovery Date:
                    <input type="date" name="recovery" value={editedPatient.recovery} onChange={handleInputChange} />
                </label> */}
                {/* Add more input fields for other patient attributes */}
                <button type="submit">Save Changes</button>
                <button type="button" onClick={onClose}>Cancel</button>
            </form>
        </div>
    );
}

export default EditPatientForm;
