import React, { useEffect, useState } from "react";
import { fetchEvents } from "../utils/api";
import { ReferenceLine, Tooltip } from "recharts";

const EventHighlights = ({ chartData }) => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const loadEvents = async () => {
      const data = await fetchEvents();
      setEvents(data.map(e => ({ ...e, date: new Date(e["Start Date"]) })));
    };
    loadEvents();
  }, []);

  return (
    <>
      {events.map((event, index) => (
        <ReferenceLine
          key={index}
          x={event.date}
          stroke="green"
          strokeDasharray="4 4"
          label={{ position: "top", value: event["Event"], fill: "green", fontSize: 12 }}
