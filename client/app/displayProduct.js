import React from 'react';
import './displayProduct.css';

const DisplayProduct = ({ products }) => {
    if (!products || products.length === 0) {
        return <p></p>;
    }

    return (
        <div className="productTable">
            <table>
                <thead>
                    <tr>
                        <th>Site</th>
                        <th>Item Title</th>
                        <th>Price (USD)</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((product, index) => (
                        <tr key={index}>
                            <td>{product.site}</td>
                            <td><a href={product.link} target="_blank" rel="noopener noreferrer">{product.item_title_name}</a></td>
                            <td>{product.price}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DisplayProduct;
