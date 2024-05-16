import React, { useState } from 'react';
import TrajectoryForm from './components/TrajectoryForm';
import TrajectoryVisualization from './components/TrajectoryVisualization';

function App() {
  const [trajectory, setTrajectory] = useState(null);

  return (
    <div className="App">
      <h1>Welcome to the Trajectory Planner</h1>
      <TrajectoryForm setTrajectory={setTrajectory} />
      {trajectory && <TrajectoryVisualization trajectory={trajectory} />}
    </div>
  );
}

export default App;
