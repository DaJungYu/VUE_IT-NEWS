<script>
import Publisher from "../assets/news.json"

export const actions = {
  Publisher({commit}){
    this.$axios.get('../assets/news.json').then(c=>{
      commit('News',c.data);
    });
  }


  }


</script>