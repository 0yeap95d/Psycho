<template>
    <div class=test-body>
        <div class=test-container>
            <span class="test-count">71441670</span>
            <span class="test-count">2130735</span>
            <span class="test-count">4523383</span>
            <span class="test-count">9332313</span>
        </div>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css?family=Montserrat');

.test-body {
    font-family: Montserrat;
    font-size: 12px;
    text-align: center;
    padding: 50px;
    background: #1c1c1c;
    display: flex;
    align-items: center;
    justify-content: center;
} 

.test-count {
  display: block;
  font-size: 24px;
  color: #f2f2f2;
  padding: 60px;
  font-weight: 600;
  width: 120px;
}

.test-container {
  display: flex;
}
</style>