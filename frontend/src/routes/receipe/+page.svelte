<script>
    let data = "receipe";
    import { fetchData } from "$lib/fetchData.js";

    let categories = [];

    fetchData("foods/categories", "GET")
        .then(response => {
            categories = response;
        })
        .catch(error => {
            console.error("Error fetching categories:", error);
        });
</script>

<b>{data}</b>

<div class="mt-16 px-3">
    {#if categories.length === 0}
        <b>Loading...</b>
    {:else}
        {#each categories as category}
            <div>
                <b>{category.name}</b>
            </div>
        {/each}
    {/if}
</div>
