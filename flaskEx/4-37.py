>>> collection.User.find( { $or: [ { price: { $ne: 1.99 } }, { qty: 20 } } ] } )