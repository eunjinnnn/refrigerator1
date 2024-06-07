<script>
    import { onMount } from 'svelte';
    import { fetchData } from "$lib/fetchData.js";

    let categories = [];

    onMount(async () => {
        try {
            const response = await fetchData("foods/categories", "GET");
            categories = response;
        } catch (error) {
            console.error("Error fetching categories:", error);
        }
    });
</script>

<div class="mt-16 px-3">
    {#if categories.length === 0}
        <b>Loading...</b>
    {:else}
        {#each categories as category}
            <div>
                <img src={category.img_url} class="h-6 sm:h-5" alt="ICON" />
                <b>{category.name}</b>
            </div>
        {/each}
    {/if}
</div>
