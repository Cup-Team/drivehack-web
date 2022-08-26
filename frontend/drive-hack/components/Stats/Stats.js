import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);
const labels = [
  "Lit Motors",
  "Hammerhead",
  "Boxbee",
  "Faraday Bicycles",
  "Moveline",
  "Mozio",
  "Shutl",
];
const data = {
  labels: labels,
  datasets: [
    {
      label: "Transport startups",
      data: [12, 7, 5, 8, 3, 6, 7],
      backgroundColor: "#652FFF",
    },
  ],
};

const Stats = () => {
  return (
    <div style={{ width: "50vw" }}>
      <Bar data={data} />
    </div>
  );
};

export default Stats;
