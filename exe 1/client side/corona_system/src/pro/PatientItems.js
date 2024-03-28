// const patientData = {{id: "123456789", firstName: "avi", lastName: "choen",
//                      addres: {city: "jerusalem", street: "srtaus", huoseNumber: 10},
//                      dateOfBirth: "1.1.2000", phone: "02-1234567", mobilePhone: "055-1234567"},}
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BASE_URL } from './config';


function PatientItems({ id }) {
	const [patientData, setPatientData] = useState({});
	useEffect(() => {
		const fetchData = async () => {
			try {
				await axios.get(`${BASE_URL}/patients_details_controller/get_by_id/${id}`)
					.then(response => {
						console.log(response.data);
						setPatientData(response.data);
						console.log(patientData);
					});
			} catch (error) {
				console.error('Error fetching data:', error);
			}
		};
		fetchData()
	}, []);


	return (
		<div className="App">
			<table>
				<tr>
					<th>טלפון ניד</th>
					<th>טלפון</th>
					<th>תאריך לידה</th>
					<th>כתובת</th>
					<th>מספר זהות</th>
					<th>שם פרטי</th>
					<th>שם משפחה</th>
				</tr>
				<tr>
					<td>{patientData.mobilePhone}</td>
					<td>{patientData.phone}</td>
					<td>{patientData.dateOfBirth}</td>
					<td>
						<table>
							<tbody>
								<tr><td>{patientData.address?.city}</td></tr>
								<tr><td>{patientData.address?.street}</td></tr>
								<tr><td>{patientData.address?.houseNumber}</td></tr>
							</tbody>
						</table>
					</td>
					<td>{patientData.id}</td>
					<td>{patientData.firstName}</td>
					<td>{patientData.lastName}</td>
				</tr>
				{/* {patientData.map((val, key) => {
					return (
						<tr key={key}>
							<td>{val.mobilePhone}</td>
							<td>{val.phone}</td>
							<td>{val.dateOfBirth}</td>
							<td>
								<table>
									<tr>{val.addres.city}</tr>
									<tr>{val.addres.street}</tr>
									<tr>{val.addres.huoseNumber}</tr>
								</table>
							</td>
							<td>{val.id}</td>
							<td>{val.firstName}</td>
							<td>{val.lastName}</td>
						</tr>
					) 
				})}*/}
			</table>
		</div>
	);
}
export default PatientItems;