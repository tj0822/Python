>>> collection.User.find( { $and: [ { price: { $ne: 1.99 } }, { qty: 20 } } ] } )