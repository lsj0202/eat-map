import { useState } from "react";
import Map from "@/components/Map";
import Markers from "@/components/Markers";
import * as stores from "@/data/store_data.json";
import StoreBox from "@/components/StoreBox";

const Home = () => {
  const [map, setMap] = useState(null);
  const [currentStore, setSurrentStore] = useState(null);
  const storeDatas = stores["DATA"];
  return (
    <>
      <Map setMap={setMap} />
      <Markers
        storeDatas={storeDatas}
        map={map}
        setSurrentStore={setSurrentStore}
      />
      <StoreBox store={currentStore} setStore={setSurrentStore} />
    </>
  );
};

export default Home;
