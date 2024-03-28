import { useState } from "react";
import axios from 'axios';
import { BASE_URL } from './config';

function AddPatientForm({onClose}) {
  const [newPatient, setNewPatient] = useState({ "id": "", "corona_vaccines": [], "recovery": "", "positive": "" });

  const handleAddInput = (e) => {
    const { name, value } = e.target;
    setNewPatient({ ...newPatient, [name]: value });
  };

  const handleSubmit = async () => {
    try {
      await axios.post(`${BASE_URL}/corona_patient_controller/add_patient`, newPatient, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      onClose();
    } catch (error) {
      console.error('Error adding patient:', error);
    };
  };


  return (
    <div className="add-patient-form">
      <h2>Add Patient</h2>
      <form onSubmit={handleSubmit}>
      <label>
          id:
          <input type="text" name="id" value={newPatient.id} onChange={handleAddInput} />
        </label>
        <label>
          Recovery Date:
          <input type="date" name="recovery" value={newPatient.recovery} onChange={handleAddInput} />
        </label>
        <label>
          Positive Date:
          <input type="date" name="positive" value={newPatient.positive} onChange={handleAddInput} />
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
        <button type="submit">Save</button>
        <button type="button" onClick={onClose}>Cancel</button>
      </form>
    </div>
  );
}
export default AddPatientForm