import React, { useState } from 'react';

const TrajectoryForm = () => {
  const [formData, setFormData] = useState({
    target_depth: '',
    deviation_angle: '',
    azimuth: '',
    curvature: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('/api/trajectory', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    });
    const data = await response.json();
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Target Depth:
        <input type="number" name="target_depth" value={formData.target_depth} onChange={handleChange} required />
      </label>
      <label>
        Deviation Angle:
        <input type="number" name="deviation_angle" value={formData.deviation_angle} onChange={handleChange} required />
      </label>
      <label>
        Azimuth:
        <input type="number" name="azimuth" value={formData.azimuth} onChange={handleChange} required />
      </label>
      <label>
        Curvature:
        <input type="number" name="curvature" value={formData.curvature} onChange={handleChange} required />
      </label>
      <button type="submit">Submit</button>
    </form>
  );
};

export default TrajectoryForm;
