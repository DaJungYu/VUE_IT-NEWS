<script>
import Publisher from "../assets/news.json"

export default {
  name: "Publisher",
  computed: {
    users() { // #1
      return Publisher.users.map((items) => { // #2
        // #3 
          let c = new Date(items["date"]); 
          let date = c.getHours()+"시 "+c.getMinutes()+"분"; 

          items["date"] = date;
          
        return items;
      })
    },
  }
};
</script>