const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: process.env.NODE_ENV === 'production'
    ? '/townsquarebr/' // Change this to your exact GitHub repo name
    : '/'
})
