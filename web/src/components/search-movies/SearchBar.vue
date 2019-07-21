<template>
    <div class='search-container'>  
        <input v-model='query' class='search-input' type='text' placeholder='Search something..' />
        <router-link :to="'/search/'+this.query">
        <button class='search-confirm' :disabled='this.query.length === 0'> Go! </button>
        </router-link>
    </div>
</template>

<script>
export default {
    name: 'SearchBar',
    data: () => {
      return {
        query: ''
      }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap');
.search-container {
    margin-top: 5px;
    display: flex;
}

.search-input {
    width: 100%;
    padding: 5px 10px;
    font-size: 1.25em;
    font-family: 'Montserrat';
    border: 1px solid rgb(126, 126, 131);
}

.search-confirm {
    font-family: 'Montserrat';
    background-color: white;
    margin-left: 10px;
    font-size: 1.25em;
    color: rgb(126, 126, 131);
    border: 1px solid rgb(126, 126, 131);
    padding: 5px 15px;
    cursor: pointer;
}

.search-confirm:hover {
    animation: color_change .5s;
    background-color: rgb(126, 126, 131);
    color: white;
}

@keyframes color_change {
    from {
        background-color: white;
    }
    to {
        background-color: rgb(126, 126, 131);
    }
}
</style>
