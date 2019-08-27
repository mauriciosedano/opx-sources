var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: './myapp/static/js/main.js',
  output: {
      path: path.resolve('./myapp/static/webpack_bundles/'),
      filename: "[name].js"
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],

  resolve: {
    alias: {
      'vue': 'vue/dist/vue.js'
    }
  }
}