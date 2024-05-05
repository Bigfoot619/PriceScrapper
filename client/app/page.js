"use client";

import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useState } from 'react';

const Home = () => {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [responseMessage, setResponseMessage] = useState('');

  const onSubmit = async (data) => {
    try {
      const response = await axios.get(`http://localhost:8000/?item=${data}`);
      setResponseMessage("Searching for product: " + response.data);
    } catch (err) {
      setResponseMessage("This product does not exist. Try again!");
    }
  };

  return (
    <>
      <div className="findProduct">
        <h1>PriceScrapper</h1>
        <form id="productForm" onSubmit={handleSubmit(onSubmit)}>
          <p>Enter Product</p>
          <input {...register('product', { required: true })} />
          {errors.product && <span>This field is required</span>}
          <p>
            <button type="submit">Search</button>
          </p>
        </form>
        {responseMessage && <p className="responseMessage">{responseMessage}</p>}
      </div>
    </>
  );
};

export default Home;