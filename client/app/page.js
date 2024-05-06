"use client";

import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useState } from 'react';
import DisplayProduct from './displayProduct';
import './page.css'

const Home = () => {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [responseMessage, setResponseMessage] = useState('');
  const [products, setProducts] = useState([]);

  const onSubmit = async (data) => {
    try {
      setResponseMessage("Searching " + data.product + "...");
      setProducts([]);
      const response = await axios.get(`http://127.0.0.1:8000/?item=${data.product}`);
      setProducts(response.data[0]);
      setResponseMessage("Your product details:")
    } catch (err) {
      setProducts([]);
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
        <DisplayProduct products={products} />
      </div>
    </>
  );
};

export default Home;