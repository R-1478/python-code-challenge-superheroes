import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function Hero() {
  const [{ data: hero, error, status }, setHero] = useState({
    data: null,
    error: null,
    status: "pending",
  });
  const { id } = useParams();

  useEffect(() => {
    fetch(`/heroes/${id}`).then((r) => {
      if (r.ok) {
        r.json().then((hero) =>
          setHero({ data: [hero], error: null, status: "resolved" })
        );
      } else {
        r.json().then((err) =>
          setHero({ data: null, error: err.error, status: "rejected" })
        );
      }
    });
  }, [id]);

  if (status === "pending") return <h1>Loading...</h1>;
  if (status === "rejected") return <h1>Error: {error.error}</h1>;

  return (
    <section>
      <h2>{hero[0].super_name}</h2>
      <h2>AKA {hero[0].name}</h2>

      <h3>Powers:</h3>
      {hero[0].powers ? ( // Check if hero[0].powers is defined
        <ul>
          {hero[0].powers.map((power) => (
            <li key={power.id}>
              <Link to={`/powers/${power.id}`}>{power.name}</Link>
            </li>
          ))}
        </ul>
      ) : (
        <p>No powers available</p>
      )}

      <Link to="/hero_powers/new">Add Hero Power</Link>
    </section>
  );
}

export default Hero;